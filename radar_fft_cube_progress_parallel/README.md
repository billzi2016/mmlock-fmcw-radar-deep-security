# Radar FFT Cube Progress Parallel

这个目录给 `adc_data_Raw_0.bin` 这类 TI mmWave Studio / DCA1000 采集文件准备一个工程化并行处理流程。目标是把 IWR6843 原始 ADC bin 拆成 frame 级任务，并行完成三层 FFT，最后批量生成点云样本。

## 实验机器

实验室工作站使用 AMD Ryzen Threadripper PRO 5995WX。并行程序默认只使用 `cpu_count() // 2` 个进程，在 128 线程机器上通常是 64 个 worker，避免长时间满载 128 线程导致机器过热。

| 参数项 | 具体规格 |
| --- | --- |
| 处理器 | AMD Ryzen Threadripper PRO 5995WX |
| 核心数量 | 64 核心 |
| 线程数量 | 128 线程 |
| 核心架构 | Zen 3 |
| 工艺制程 | 7nm |
| 基准频率 | 2.7 GHz |
| 最高加速频率 | 4.5 GHz |
| 三级缓存 L3 | 256 MB |
| 热设计功耗 TDP | 280W |
| 内存通道支持 | 8 通道 DDR4 |

## 数据规模

论文实验中的点云样本规模可以按以下方式理解：

```text
参与人数：16 人
设计姿态：34 种静态姿态
单人单姿态：每人对每个姿态采集 1500 帧，生成约 100 个点云样本
总点云样本：16 × 34 × 100 = 54,400
```

后续如果继续采集新数据，程序仍按 frame/sample 级任务切分，适合扩展到数十万个样本。

## 目录结构

```text
radar_fft_cube_progress_parallel/
├── README.md
├── run_parallel_fft.py
└── src/
    ├── __init__.py
    ├── config.py
    ├── dca1000_reader.py
    ├── fft_layers.py
    ├── parallel_pipeline.py
    └── point_cloud.py
```

## 处理流程

```text
adc_data_Raw_0.bin
  -> frame-wise DCA1000 reader
  -> range FFT
  -> Doppler FFT
  -> angle FFT
  -> threshold/CFAR-style point extraction
  -> per-frame point_cloud_XXXXXX.npz
```

三层 FFT 拆分在 `src/fft_layers.py` 中：

- `range_fft()`：对 ADC fast-time sample 维做 FFT，得到 range bins。
- `doppler_fft()`：对 slow-time loop 维做 FFT，得到 Doppler bins。
- `angle_fft()`：对 virtual antenna 维做 FFT，得到 angle bins。

并行入口在 `src/parallel_pipeline.py` 中，使用 `multiprocessing.Pool`。默认 worker 数来自：

```python
workers = max(1, (os.cpu_count() or 2) // 2)
```

## 使用方式

把 `adc_data_Raw_0.bin` 放在当前目录，或通过参数指定路径：

```bash
python run_parallel_fft.py \
  --adc-bin adc_data_Raw_0.bin \
  --output-dir outputs/point_clouds \
  --num-frames 1000
```

如果要处理全部完整 frame，可以不传 `--num-frames`：

```bash
python run_parallel_fft.py \
  --adc-bin adc_data_Raw_0.bin \
  --output-dir outputs/point_clouds
```

默认并行进程数为 CPU 线程数的一半。也可以手动指定：

```bash
python run_parallel_fft.py \
  --adc-bin adc_data_Raw_0.bin \
  --output-dir outputs/point_clouds \
  --workers 64
```

## 参数提醒

`src/config.py` 里的雷达参数必须和 mmWave Studio 的真实 profile/chirp/frame 配置一致，尤其是：

- `num_adc_samples`
- `num_rx`
- `num_tx`
- `num_loops_per_frame`
- `sample_rate_hz`
- `slope_hz_per_s`
- `start_freq_hz`
- `chirp_period_s`

参数不匹配时，轻则 reshape 失败，重则点云距离、速度和角度全部偏移。

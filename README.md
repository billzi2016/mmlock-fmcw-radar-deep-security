# mmLock FMCW Radar Deep Security

## Overview

mmLock FMCW Radar Deep Security is a millimeter-wave radar sensing project for device-security scenarios. It centers on user-leaving detection, anti-data-theft protection, and high-quality mmWave radar imaging. The repository is organized around public paper materials and highlights three core directions: FMCW radar sensing, deep learning modeling, and security protection.

**Tags**: `fmcw` · `deeplearning` · `security` · `mmwave-radar` · `point-cloud`

## Documentation Site

GitHub Pages: https://billzi2016.github.io/mmlock-fmcw-radar-deep-security/

The documentation site is maintained in `docs-site/`. It explains the project from wireless sensing and radar basics to FMCW sensing, mmLock paper reading, FFT processing, point-cloud generation, and the CNN + BiLSTM model workflow. The wireless-sensing page also compares WiFi CSI sensing with FMCW radar sensing.

## Paper

- Repository PDF: [`C61.pdf`](C61.pdf)
- Title: *mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging*
- Authors: Jiawei Xu, Ziqian Bi, Amit Singha, Tao Li, Yimin Chen, Yanchao Zhang
- Venue: 2023 32nd International Conference on Computer Communications and Networks (ICCCN)
- DOI: https://doi.org/10.1109/ICCCN58024.2023.10230151
- ASU record: https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/
- Public PDF source: [ASU CNSG public PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

## Notebooks

| Notebook | Purpose |
| --- | --- |
| [`mmlock_c61_paper_reading_zh.ipynb`](mmlock_c61_paper_reading_zh.ipynb) | Chinese paper-reading notebook for mmLock, covering the system flow, threat model, FFT, point-cloud generation, PointNet/LSTM ideas, and experiment notes. |
| [`radar_fft_cube_progress.ipynb`](radar_fft_cube_progress.ipynb) | Step-by-step radar signal-processing notebook from DCA1000 raw ADC bin data to TDM-MIMO frame cube, Range/Doppler/Angle FFT, and point detection. |
| [`cnn_blstm_pointcloud_training.ipynb`](cnn_blstm_pointcloud_training.ipynb) | Point-cloud sequence modeling notebook that prepares radar point sequences and trains a CNN + BiLSTM classifier. |

## Related Code Repositories

- Radar data-processing platform: [mmwave-fmcw-cascade-mimo-sensing-platform](https://github.com/billzi2016/mmwave-fmcw-cascade-mimo-sensing-platform)
- MIMO FMCW radar simulator: [MIMO-FMCW-Radar-Simulator-Multiprocess](https://github.com/billzi2016/MIMO-FMCW-Radar-Simulator-Multiprocess)

These repositories are useful companions to this project: the first one is closer to real mmWave FMCW radar data processing, while the second one helps explain and test MIMO FMCW radar concepts in a simulator setting.

## Project Goals

- Organize the mmLock paper and related materials into a presentable and maintainable FMCW radar security project repository.
- Highlight the engineering value of millimeter-wave FMCW radar for security sensing.
- Preserve room for future expansion, including code reproduction, model-architecture notes, data-processing workflows, and experiment logs.

## Core Capabilities

- User-leaving detection: use millimeter-wave radar to detect when a user leaves, providing a trigger for automatic screen lock and data protection.
- High-quality radar imaging: structure the repository around mmWave radar imaging and 3D human point-cloud or mesh representations.
- Deep-learning-based recognition: apply deep learning models to radar sensing data for behavior recognition and security judgment.
- Security-oriented deployment: target data-theft protection use cases in end devices, office devices, and smart spaces.

## Technology Stack

- FMCW mmWave radar sensing
- Radar imaging and point-cloud processing
- Deep learning for behavior recognition
- Security-oriented user presence detection

## Project Structure

```text
mmlock-fmcw-radar-deep-security/
├── C61.pdf
├── citation.bib
├── cnn_blstm_pointcloud_training.ipynb
├── docs-site/
│   ├── docs/
│   ├── mkdocs.yml
│   └── requirements.txt
├── img/
│   ├── embedded/
│   └── pages/
├── mmlock_c61_paper_reading_zh.ipynb
├── radar_fft_cube_progress.ipynb
├── radar_fft_cube_progress_parallel/
│   ├── README.md
│   ├── run_parallel_fft.py
│   └── src/
├── README.md
└── .gitignore
```

## How to Use

At the current stage, the repository mainly serves as a paper-material archive and project description. It does not yet provide a complete runnable pipeline at the repository root. If executable code is expanded later, the README can be updated with environment setup, data preparation, training workflow, and reproduction instructions.

## Current Progress

- The paper PDF has been archived.
- An independent project directory has been established.
- Project description, technical tags, and source information have been added.
- A GitHub Pages documentation site has been added under `docs-site/`.
- A notebook workflow from raw ADC bin data to radar FFT cube and point cloud has been added.
- A multiprocessing framework for large-scale sample processing has been added.
- Paper figures have been extracted into `img/`, and a Chinese notebook with paragraph-by-paragraph reading notes has been added.
- A CNN + BiLSTM notebook based on the parallel FFT point-cloud output format has been added.

## Next Steps

- Add a system architecture diagram and data-flow description.
- Organize the FMCW radar data-processing pipeline.
- Add deep-learning model architecture notes and training/inference workflows.
- Expand the security scenario description, threat model, and applicability boundaries.
- If code is opened further, add installation, runtime, and experiment-reproduction documentation.

## Paper Source and Copyright Notes

Paper file: [`C61.pdf`](C61.pdf)

Paper title: *mmLock: User Leaving Detection Against Data Theft via High-Quality mmWave Radar Imaging*

Authors: Jiawei Xu, Ziqian Bi, Amit Singha, Tao Li, Yimin Chen, Yanchao Zhang

Conference: *2023 32nd International Conference on Computer Communications and Networks (ICCCN), 2023*

The Google Scholar entry can be identified as:

```text
mmLock: User leaving detection against data theft via high-quality mmWave radar imaging
J Xu, Z Bi, A Singha, T Li, Y Chen, Y Zhang
2023 32nd International Conference on Computer Communications and Networks ..., 2023
```

BibTeX:

```bibtex
@inproceedings{xu2023mmlock,
  title={mmLock: User leaving detection against data theft via High-Quality mmWave Radar Imaging},
  author={Xu, Jiawei and Bi, Ziqian and Singha, Amit and Li, Tao and Chen, Yimin and Zhang, Yanchao},
  booktitle={2023 32nd International Conference on Computer Communications and Networks (ICCCN)},
  pages={1--10},
  year={2023},
  organization={IEEE},
  doi={10.1109/ICCCN58024.2023.10230151},
  url={https://doi.org/10.1109/ICCCN58024.2023.10230151}
}
```

ASU paper record: `https://asu.elsevierpure.com/en/publications/mmlock-user-leaving-detection-against-data-theft-via-high-quality/`

Public source: [ASU CNSG public PDF](https://labs.engineering.asu.edu/cnsg/wp-content/uploads/sites/147/2024/02/C61.pdf)

DOI: `https://doi.org/10.1109/ICCCN58024.2023.10230151`

The paper PDF in this repository is preserved as author-owned paper material for project archiving, engineering notes, and academic presentation. The ASU CNSG website provides a public PDF link, and the ASU official paper record also includes the paper and DOI information.

For NSF-supported peer-reviewed papers or formal conference papers, the NSF Public Access Policy requires the relevant paper version to enter the designated public-access repository and become publicly accessible within the required time window. This repository preserves the ASU public source, ASU paper record, and DOI so that the formal publication information and public-access source can be traced.

Copyright, publisher-version status, and redistribution permissions still depend on IEEE policies, the author publication agreement, the ASU public page, and the relevant NSF public-access policy. When citing, distributing, or redistributing the work, the formal publication record and the public-source links above should be preferred.

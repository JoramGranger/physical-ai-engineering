# Learning resources and verification register

Last reviewed **2026-11-23**. Links below were opened using browsing against university, author, publisher, project, or vendor sites. “Verified” means the linked page and its identity were accessible; it does not promise access to every video, assignment, or download. Restricted course platforms may require enrollment.

Reading selections in this repository are organized by topic. They are our study recommendations, not quoted lecture titles or claims about lecture numbering. Follow the source's current contents to locate the topic. No unverified lecture numbers or textbook chapter numbers are assigned.

## University lectures and course materials

| ID | Official resource | Use | Access review |
| --- | --- | --- | --- |
| CS229 | [Stanford CS229 — Machine Learning, SEE archive](https://see.stanford.edu/Course/CS229) | M1–2: mathematical ML foundations | Verified; public archive with lectures/notes |
| CS230 | [Stanford CS230 — Deep Learning](https://cs230.stanford.edu/) | M2: neural networks and training practice | Verified; public page links archived videos; some current materials restricted |
| CS231N | [Stanford CS231n — Deep Learning for Computer Vision, 2025](https://cs231n.stanford.edu/2025/) | M2–3: visual recognition | Verified; public materials; current recordings may require Canvas |
| CS231A | [Stanford CS231A — Computer Vision](https://web.stanford.edu/class/cs231a/) | M4: geometric vision and reconstruction | Verified; public syllabus/notes |
| MIT-VISION | [MIT 6.801 — Machine Vision, Fall 2020](https://ocw.mit.edu/courses/6-801-machine-vision-fall-2020/) | M3–4: image formation and classical vision | Verified; archived OCW notes and assignments; do not assume video coverage |
| MIT-CONTROL | [MIT Underactuated Robotics](https://underactuated.mit.edu/) | M5, M8, M10–12: dynamics, control, optimization | Verified; notes and links to lectures |
| PRINCETON | [Princeton — Introduction to Robotics](https://irom-lab.princeton.edu/intro-to-robotics/) | M5–8: robot modeling and autonomy | Verified; public-facing course site with lecture resources |
| MODERN | [Northwestern — Modern Robotics video supplements](https://modernrobotics.northwestern.edu/nu-gm-book-resource/) | M5–6, M11–12: mechanics, planning, control | Verified; public video index |
| CS336 | [Stanford CS336 — Language Modeling from Scratch](https://cs336.stanford.edu/) | M9: selective language-model systems study | Verified; elective selections, not a whole additional course |
| CS285 | [UC Berkeley CS185/285 — Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/) | M10: policy learning and imitation | Verified; use public material from the available offering |

## Foundational books

| ID | Book and author/publisher link | Study use | Access review |
| --- | --- | --- | --- |
| MML | [Mathematics for Machine Learning — Deisenroth, Faisal, Ong](https://mml-book.github.io/) | Linear algebra, calculus, probability, optimization | Verified; author-hosted book materials |
| DL | [Deep Learning — Goodfellow, Bengio, Courville](https://www.deeplearningbook.org/) | Neural networks and learning theory | Verified; online book |
| SZELISKI | [Computer Vision: Algorithms and Applications — Richard Szeliski, second edition](https://szeliski.org/Book/) | Image processing, recognition, geometry | Verified; personal-use download through author's page; do not redistribute |
| MVG | [Multiple View Geometry in Computer Vision — Hartley and Zisserman, second edition](https://www.robots.ox.ac.uk/~vgg/hzbook/) | Projective geometry, epipolar constraints, reconstruction | Verified; companion materials and sample chapters; full book may require library/purchase |
| MR | [Modern Robotics: Mechanics, Planning, and Control — Lynch and Park](https://modernrobotics.org/) | Rigid motion, kinematics, dynamics, control | Verified; redirects to Northwestern book page with preprint/resources |
| PR | [Probabilistic Robotics — Thrun, Burgard, Fox](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) | Bayesian estimation, localization, mapping | Verified publisher page; library/purchase may be needed |

Use library access before purchasing. These are references across the year; reading all six cover to cover is not required.

## Engineering documentation

| ID | Official resource | Use and version caveat | Access review |
| --- | --- | --- | --- |
| PYTORCH | [PyTorch tutorials](https://docs.pytorch.org/tutorials/) | Training, autograd, profiling, export; match installed release | Verified |
| OPENCV | [OpenCV 4.x documentation](https://docs.opencv.org/4.x/) | Image processing, calibration, video; rolling 4.x alias | Verified; redirects to a concrete version |
| ROS2 | [ROS 2 Jazzy documentation](https://docs.ros.org/en/jazzy/) | Nodes, communication, frames, bag replay | **Content access unverified:** browsing blocked by anti-bot page; official endpoint confirmed through Open Robotics release announcement below |
| ROS-BASELINE | [Open Robotics — Jazzy release announcement](https://www.openrobotics.org/blog/2024/5/ros-jazzy-jalisco-released) | Ubuntu 24.04 / Jazzy / Harmonic pairing | Verified official search result; corroborated by Gazebo page |
| GAZEBO | [Gazebo Harmonic — Installing Gazebo with ROS](https://gazebosim.org/docs/harmonic/ros_installation/) | Distribution compatibility and simulation setup | Verified |
| NAV2 | [Nav2 Jazzy documentation](https://docs.nav2.org/jazzy/) | Mobile navigation integration | Verified; use Jazzy documentation rather than rolling defaults |
| MOVEIT | [MoveIt 2 documentation](https://moveit.picknik.ai/main/index.html) | Manipulation concepts and planning | Verified **rolling** page; select instructions compatible with installed ROS release before executing |
| PX4 | [PX4 v1.17 documentation](https://docs.px4.io/v1.17/en/) | SITL, offboard control, mission/failsafe concepts | Verified versioned documentation; pin actual firmware tag/commit in each run |
| ESP-IDF | [ESP-IDF — ESP32 programming guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/) | GPIO, buses, timers, firmware | Verified; select actual SoC and record SDK version |
| DOCKER | [Docker documentation](https://docs.docker.com/) | Reproducible development and services | Verified |
| APPTAINER | [Apptainer user guide](https://apptainer.org/docs/user/main/) | HPC container execution | Verified; rolling guide; match cluster installation |
| ONNX | [ONNX documentation](https://onnx.ai/onnx/) | Graph interchange and model validation | Verified; record exporter/opset/runtime versions |
| TENSORRT | [NVIDIA TensorRT documentation](https://docs.nvidia.com/deeplearning/tensorrt/latest/) | Target-specific inference optimization | Verified; rolling documentation; confirm device support matrix |
| OPENVLA | [OpenVLA project and paper](https://openvla.github.io/) | M10: a concrete VLA research example | Verified; inspect compute/data/action assumptions before attempting reproduction |

## Maintaining this register

When a URL changes, open the authoritative replacement, record the review date and access limitations, and update dependent course links. A successful HTTP response alone can be a login or anti-bot page. Read the page identity before marking it verified.

Dataset and model acquisition belongs to each project implementation. Record the specific dataset/model release, license, source URL, hash, permitted use, and split method then; none is downloaded or licensed implicitly by this repository.

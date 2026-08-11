<div align="center">
  <h1>Awesome Agentic Artifact Creation</h1>
  <p>
    A curated list of papers on agentic systems that plan, generate, inspect,
    revise, and maintain artifacts.
  </p>
</div>

---

This catalog navigates work by the artifact being constructed and records
application context as a separate, optional classification axis. It does not
mix workflow stage or evaluation setup into the artifact hierarchy. It
accompanies the
[Agentic Artifact Creation survey](https://github.com/GeminiLight/agentic-creation-survey)
and follows the survey's artifact-centered landscape.

The initial release re-audits the survey's candidate systems and benchmarks
against an operational agentic-construction rule. The public list contains only
accepted entries; pending and excluded decisions remain visible in
[`data/audit.csv`](data/audit.csv) and the [audit protocol](AUDIT.md).

## Survey Scope

- **Textual Artifacts:** creative writing, professional documents, reports, and
  scholarly writing.
- **2D Visual Artifacts:** data visualizations, diagrams, images, posters, and
  presentations.
- **Audio Artifacts:** music composition and produced or spoken audio.
- **Video Artifacts:** expository and narrative video, plus video
  editing and repair.
- **Spatial Artifacts:** objects, scenes, worlds, CAD, and engineering
  geometry.
- **Behavioral Artifacts:** repositories, applications, websites,
  user interfaces, games, and simulations.

The application axis currently covers creative production, brand communication,
educational support, professional work, scientific research, and engineering
design. Application subdomains remain blank until a controlled vocabulary is
defined.

The catalog considers representative venues across AI, computing, design, and
domain research. The list is indicative rather than exhaustive; relevant
workshops, journals, and preprints are also considered. Representative venues
already covered by this release include:

- **Artificial Intelligence:** AAAI and IJCAI.
- **Machine Learning:** NeurIPS, ICML, ICLR, and TPAMI.
- **Natural Language Processing:** ACL, EMNLP, NAACL, COLM, EACL, and Findings
  tracks.
- **Computer Vision:** CVPR, ICCV, and ECCV.
- **Graphics and Visualization:** SIGGRAPH, SIGGRAPH Asia, and IEEE VIS/TVCG.
- **Human–Computer Interaction:** CHI, UIST, CSCW, and TOCHI.
- **Data Mining and Information Retrieval:** KDD, The Web Conference, SIGIR,
  and SIGMOD.
- **Software and Engineering:** ICSE, FSE, ISSTA, EASE, DATE, and ASME
  IDETC-CIE.
- **Audio and Interdisciplinary Research:** ICASSP, ISMIR, Digital Discovery,
  and IEEE Transactions on Learning Technologies.

## Catalog Analysis

- **177 included papers** spanning **2024–2026**.
- **162 artifact systems** and **15 artifact benchmarks**.
- **6 artifact families**, **15 artifact types**, and **6 application contexts**.
- **153 included papers** currently carry an application classification.

*Sources: generated `data/papers.csv`, `data/taxonomy.json`, and `data/venues.csv`.*

> [!NOTE]
> Counts describe this audited catalog rather than total field output. The audit
> is a structured first pass, and 2026 is an incomplete publication year.

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before
adding or reclassifying a paper.

## Content

<table>
<tr><th colspan="3"><a href="#artifact-centered-view">📦 Artifact-centered View</a></th></tr>
<tr><td colspan="3"><strong><a href="#textual-artifacts">1. Textual Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#creative-writing">1.1. Creative Writing</a></td>
<td>&emsp;<a href="#professional-documents">1.2. Professional Documents</a></td>
<td>&emsp;<a href="#scholarly-manuscripts">1.3. Scholarly Manuscripts</a></td>
</tr>
<tr><td colspan="3"><strong><a href="#2d-visual-artifacts">2. 2D Visual Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#data-visualizations">2.1. Data Visualizations</a></td>
<td>&emsp;<a href="#illustrative-graphics">2.2. Illustrative Graphics</a></td>
<td>&emsp;<a href="#visual-documents">2.3. Visual Documents</a></td>
</tr>
<tr><td colspan="3"><strong><a href="#audio-artifacts">3. Audio Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#music">3.1. Music</a></td>
<td>&emsp;<a href="#spoken-audio">3.2. Spoken Audio</a></td>
<td></td>
</tr>
<tr><td colspan="3"><strong><a href="#video-artifacts">4. Video Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#expository-videos">4.1. Expository Videos</a></td>
<td>&emsp;<a href="#narrative-videos">4.2. Narrative Videos</a></td>
<td>&emsp;<a href="#video-editing-and-repair">4.3. Video Editing and Repair</a></td>
</tr>
<tr><td colspan="3"><strong><a href="#spatial-artifacts">5. Spatial Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#3d-assets">5.1. 3D Assets</a></td>
<td>&emsp;<a href="#3d-scenes">5.2. 3D Scenes</a></td>
<td></td>
</tr>
<tr><td colspan="3"><strong><a href="#behavioral-artifacts">6. Behavioral Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#software-systems">6.1. Software Systems</a></td>
<td>&emsp;<a href="#simulation-models">6.2. Simulation Models</a></td>
<td></td>
</tr>
<tr><th colspan="3"><a href="#application-centered-view">🎯 Application-centered View</a></th></tr>
<tr>
<td>&emsp;<a href="#creative-production">A.1. Creative Production</a></td>
<td>&emsp;<a href="#brand-communication">A.2. Brand Communication</a></td>
<td>&emsp;<a href="#educational-support">A.3. Educational Support</a></td>
</tr>
<tr>
<td>&emsp;<a href="#professional-work">A.4. Professional Work</a></td>
<td>&emsp;<a href="#scientific-research">A.5. Scientific Research</a></td>
<td>&emsp;<a href="#engineering-design">A.6. Engineering Design</a></td>
</tr>
</table>

<a id="artifact-centered-view"></a>

## [Textual Artifacts](#content)

### [Creative Writing](#content)

#### [Narratives](#content)

1. **StoryBox: Collaborative Multi-Agent Simulation for Hybrid Bottom-Up Long-Form Story Generation Using Large Language Models**

    *Zehao Chen, Rong Pan, Haoran Li*

    AAAI, 2026. [Published](https://ojs.aaai.org/index.php/AAAI/article/view/40288) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

2. **Constella: Supporting Storywriters’ Interconnected Character Creation through LLM-Based Multi-Agents**

    *Syemin Park, Soobin Park, Youn-kyung Lim*

    ACM TOCHI, 2026. [Published](https://doi.org/10.1145/3796234) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

3. **From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives**

    *Aayush Aluru, Chloe Ho, Muhammad Hammouri, Kerry Luo, Myra Malik, Ryan Lagasse, Arjun Bahuguna, Vasu Sharma*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.00918) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

4. **Exploring Creator-Centric Methods for LLM-Assisted Interactive Storytelling**

    *Yuelu Li, Siyi Wu, Lujin Zhang, Zhihan Guo, Wenchuan Lu, David Yip*

    CHI, 2026. [Published](https://doi.org/10.1145/3772318.3791362) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

5. **BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation**

    *Yiting Ran, Xintao Wang, Tian Qiu, Jiaqing Liang, Yanghua Xiao, Deqing Yang*

    ACL, 2025. [Published](https://aclanthology.org/2025.acl-long.773/) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

6. **CreAgentive: An Agent Workflow Driven Multi-Category Creative Generation Engine**

    *Yuyang Cheng, Linyue Cai, Changwei Peng, Yumiao Xu, Rongfang Bie, Yong Zhao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.26461) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

7. **Orchid: A Creative Approach for Authoring LLM-Driven Interactive Narratives**

    *Zhen Wu, Serkan Kumyol, Shing Yin Wong, Xiaozhu Hu, Xin Tong, Tristan Braud*

    C&C, 2025. [Published](https://doi.org/10.1145/3698061.3726906) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

8. **StoryWriter: A Multi-Agent Framework for Long Story Generation**

    *Haotian Xia, Hao Peng, Yunjia Qi, Bin Xu, Juanzi Li, Hou Lei, Xiaozhi Wang*

    CIKM, 2025. [Published](https://doi.org/10.1145/3746252.3761616) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

9. **Can LLMs Generate Good Stories? Insights and Challenges from a Narrative Planning Perspective**

    *Yi Wang, Max Kreminski*

    IEEE CoG, 2025. [Published](https://doi.org/10.1109/CoG64752.2025.11114137) · `Benchmark` · `📦 Textual Artifacts` · `🎯 Creative Production`

10. **StoryVerse: Towards Co-authoring Dynamic Plot with LLM-based Character Simulation via Narrative Planning**

    *Yi Wang, Qian Zhou, David Ledo*

    FDG, 2024. [Published](https://doi.org/10.1145/3649921.3656987) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

#### [Performative Texts](#content)

1. **Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Creative Writing**

    *Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.14770) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

2. **OpenMic: A Multi-Agent-Based Stand-Up Comedy Generation System**

    *Yuyang Wu, Hanzhong Cao, Jianhao Chen, Yufei Li*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.08288) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

### [Professional Documents](#content)

#### [Informational Reports](#content)

1. **DIAGPaper: Diagnosing Valid and Specific Weaknesses in Scientific Papers via Multi-Agent Reasoning**

    *Zhuoyang Zou, Abolfazl Ansari, Delvin Ce Zhang, Dongwon Lee, Wenpeng Yin*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.07611) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

2. **Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Verification**

    *Yi Yuan, Xuhong Wang, Shanzhe Lei*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05952) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

3. **Benchmarking Agentic Newswriting via Journalistic Workflows**

    *Yen-Che Chien, Kuang-Da Wang, Wei-Yao Wang, Wen-Chih Peng*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.1816/) · `Benchmark` · `📦 Textual Artifacts` · `🎯 Professional Work` · [Code](https://github.com/wywyWang/CoachAI-Projects)

4. **Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation on AI Research Papers**

    *Zhijian Xu, Yilun Zhao, Manasi Patwardhan, Lovekesh Vig, Arman Cohan*

    ACL, 2025. [Published](https://aclanthology.org/2025.acl-long.1009/) · `Benchmark` · `📦 Textual Artifacts` · `🎯 Scientific Research`

5. **Queryome: Orchestrating Retrieval, Reasoning, and Synthesis across Biomedical Literature**

    *Pranav Punuru, Nabil Ibtehaz, Swagarika Jaharlal Giri, Harsha Srirangam, Emilia A Tugolukova, Daisuke Kihara*

    bioRxiv, 2025. [Preprint](https://doi.org/10.64898/2025.12.22.696019) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

6. **AI-Press: A Multi-Agent News Generating and Feedback Simulation System Powered by Large Language Models**

    *Xiawei Liu, Shiyue Yang, Xinnong Zhang, Haoyu Kuang, Libo Sun, Yihang Yang, Siming Chen, Xuanjing Huang, Zhongyu Wei*

    COLING, 2025. [Published](https://aclanthology.org/2025.coling-demos.8/) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

7. **MARG: Multi-Agent Review Generation for Scientific Papers**

    *Mike D'Arcy, Tom Hope, Larry Birnbaum, Doug Downey*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2401.04259) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

8. **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models**

    *Shao, Yijia, Jiang, Yucheng, Kanell, Theodore A., Xu, Peter, Khattab, Omar, Lam, Monica S.*

    NAACL, 2024. [Published](https://aclanthology.org/2024.naacl-long.347/) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

#### [Functional Documents](#content)

1. **DocAgent: A Multi-Agent System for Automated Code Documentation Generation**

    *Dayu Yang, Antoine Simoulin, Xin Qian, Xiaoyi Liu, Yuwei Cao, Zhaopu Teng, Grey Yang*

    ACL, 2025. [Published](https://aclanthology.org/2025.acl-demo.44/) · `System` · `📦 Textual Artifacts` · `🎯 Engineering Design`

2. **AgentCTG: Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation**

    *Xinxu Zhou, Jiaqi Bai, Zhenqi Sun, Fanxiang Zeng, Yue Liu*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.13677) · `System` · `📦 Textual Artifacts`

3. **EduAgentQG: A Multi-Agent Workflow Framework for Personalized Question Generation**

    *Rui Jia, Min Zhang, Fengrui Liu, Bo Jiang, Kun Kuang, Zhongxiang Dai*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.11635) · `System` · `📦 Textual Artifacts` · `🎯 Educational Support`

4. **PAME-AI: Patient Messaging Creation and Optimization using Agentic AI**

    *Junjie Luo, Yihong Guo, Anqi Liu, Ritu Agarwal, Gordon Gao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.24263) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

5. **MADS: Multi-Agent Dialogue Simulation for Diverse Persuasion Data Generation**

    *Mingjin Li, Yu Liu, Huayi Liu, Xiang Ye, Chao Jiang, Hongguang Zhang, Yu Ruan*

    EMNLP Industry Track, 2025. [Published](https://aclanthology.org/2025.emnlp-industry.26/) · `System` · `📦 Textual Artifacts` · `🎯 Brand Communication`

6. **EduPlanner: LLM-Based Multiagent Systems for Customized and Intelligent Instructional Design**

    *Xueqiao Zhang, Chao Zhang, Jianwen Sun, Jun Xiao, Yi Yang, Yawei Luo*

    IEEE TLT, 2025. [Published](https://doi.org/10.1109/TLT.2025.3561332) · `System` · `📦 Textual Artifacts` · `🎯 Educational Support`

7. **LLM-powered Multi-agent Framework for Goal-oriented Learning in Intelligent Tutoring System**

    *Tianfu Wang, Yi Zhan, Jianxun Lian, Zhengyu Hu, Nicholas Jing Yuan, Qi Zhang, Xing Xie, Hui Xiong*

    The Web Conference Companion, 2025. [Published](https://doi.org/10.1145/3701716.3715244) · `System` · `📦 Textual Artifacts` · `🎯 Educational Support` · [Code](https://github.com/GeminiLight/gen-mentor)

8. **Translation Agent: Agentic Translation Using Reflection Workflow**

    *Andrew Ng, Joaquin Dominguez, Nedelina Teneva, John Santerre*

    GitHub, 2024. [Project](https://github.com/andrewyng/translation-agent) · `System` · `📦 Textual Artifacts`

### [Scholarly Manuscripts](#content)

1. **PaperDebugger: A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing**

    *Junyi Hou, Andre Lin Huikai, Nuo Chen, Yiwei Gong, Bingsheng He*

    The Web Conference Companion, 2026. [Published](https://doi.org/10.1145/3774905.3793122) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

2. **IdeaSynth: Iterative Research Idea Development Through Evolving and Composing Idea Facets with Literature-Grounded Feedback**

    *Kevin Pu, K. J. Kevin Feng, Tovi Grossman, Tom Hope, Bhavana Dalvi Mishra, Matt Latzke, Jonathan Bragg, Joseph Chee Chang, Pao Siangliulue*

    CHI, 2025. [Published](https://doi.org/10.1145/3706598.3714057) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

3. **ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models**

    *Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, Sung Ju Hwang*

    NAACL, 2025. [Published](https://aclanthology.org/2025.naacl-long.342/) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

4. **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery**

    *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2408.06292) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`


## [2D Visual Artifacts](#content)

### [Data Visualizations](#content)

1. **MultiVis-Agent: A Multi-Agent Framework with Logic Rules for Reliable and Comprehensive Cross-Modal Data Visualization**

    *Jinwei Lu, Yuanfeng Song, Chen Zhang, Raymond Chi-Wing Wong*

    PACMMOD (SIGMOD), 2026. [Published](https://doi.org/10.1145/3786670) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

2. **A2P-Vis: an Analyzer-to-Presenter Agentic Pipeline for Visual Insights Generation and Reporting**

    *Shuyu Gan, Renxiang Wang, James Mooney, Dongyeop Kang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.22101) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

3. **CoDA: Agentic Systems for Collaborative Data Visualization**

    *Zichen Chen, Jiefeng Chen, Sercan Ö. Arık, Misha Sra, Tomas Pfister, Jinsung Yoon*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.03194) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

4. **Jupybara: Operationalizing a Design Space for Actionable Data Analysis and Storytelling with LLMs**

    *Huichen Will Wang, Larry Birnbaum, Vidya Setlur*

    CHI, 2025. [Published](https://doi.org/10.1145/3706598.3713913) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

5. **DataWink: Reusing and Adapting SVG-based Visualization Examples with Large Multimodal Models**

    *Liwenhan Xie, Yanna Lin, Can Liu, Huamin Qu, Xinhuan Shu*

    IEEE TVCG, 2025. [Published](https://doi.org/10.1109/TVCG.2025.3634635) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

6. **PlotGen: Multi-Agent LLM-based Scientific Data Visualization via Multimodal Retrieval Feedback**

    *Kanika Goswami, Puneet Mathur, Ryan Rossi, Franck Dernoncourt*

    The Web Conference Companion, 2025. [Published](https://doi.org/10.1145/3701716.3716888) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

7. **MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization**

    *Zhiyu Yang, Zihan Zhou, Shuo Wang, Xin Cong, Xu Han, Yukun Yan, Zhenghao Liu, Zhixing Tan, Pengyuan Liu, Dong Yu, Zhiyuan Liu, Xiaodong Shi, Maosong Sun*

    Findings of ACL, 2024. [Published](https://aclanthology.org/2024.findings-acl.701/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

8. **LightVA: Lightweight Visual Analytics With LLM Agent-Based Task Planning and Execution**

    *Yuheng Zhao, Junjie Wang, Linbin Xiang, Xiaowen Zhang, Zifei Guo, Cagatay Turkay, Yu Zhang, Siming Chen*

    IEEE TVCG, 2024. [Published](https://doi.org/10.1109/TVCG.2024.3496112) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

### [Illustrative Graphics](#content)

#### [Images](#content)

1. **Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling**

    *Ruijie Ye, Jiayi Zhang, Zhuoxin Liu, Zihao Zhu, Siyuan Yang, Li Li, Tianfu Fu, Franck Dernoncourt, Yue Zhao, Jiacheng Zhu, Ryan Rossi, Wenhao Chai, Zhengzhong Tu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.09084) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

2. **CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator**

    *Yuhan Pu, Hao Zheng, Ziqian Mo, Zirui Pang, Hill Zhang, Tianyi Fan, Shuhong Wu, Jiaheng Wei*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.03156) · `System` · `📦 2D Visual Artifacts`

3. **CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration**

    *Hairui Zhu, Yiying Yang, Tengjin Weng, Ziyu Lu, Xiao Yao, Xiaoyang Ye, Lin Ma, Wenhao Jiang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.05465) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

4. **Agentic Retoucher for Text-To-Image Generation**

    *Shaocheng Shen, Jianfeng Liang, Chunlei Cai, Cong Geng, Huiyu Duan, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai*

    CVPR, 2026. [Published](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_Agentic_Retoucher_for_Text-To-Image_Generation_CVPR_2026_paper.html) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

5. **GraphicBench: A Planning Benchmark for Graphic Design with Language Agents**

    *Dayeon Ki, Tianyi Zhou, Marine Carpuat, Gang Wu, Puneet Mathur, Viswanathan Swaminathan*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2504.11571) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

6. **Mirror in the Model: Ad Banner Image Generation via Reflective Multi-LLM and Multi-modal Agents**

    *Zhao Wang, Bowen Chen, Yotaro Shimose, Sota Moriyama, Heng Wang, Shingo Takamatsu*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2507.03326) · `System` · `📦 2D Visual Artifacts` · `🎯 Brand Communication`

7. **SketchAgent: Language-Driven Sequential Sketch Generation**

    *Yael Vinker, Tamar Rott Shaham, Kristine Zheng, Alex Zhao, Judith E. Fan, Antonio Torralba*

    CVPR, 2025. [Published](https://doi.org/10.1109/CVPR52734.2025.02175) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

8. **BannerAgency: Advertising Banner Design with Multimodal LLM Agents**

    *Heng Wang, Yotaro Shimose, Shingo Takamatsu*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.214/) · `System` · `📦 2D Visual Artifacts` · `🎯 Brand Communication`

9. **T2I-Copilot: A Training-Free Multi-Agent Text-to-Image System for Enhanced Prompt Interpretation and Interactive Generation**

    *Chieh-Yun Chen, Min Shi, Gong Zhang, Humphrey Shi*

    ICCV, 2025. [Published](https://doi.org/10.1109/ICCV51701.2025.01803) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

#### [Diagrams](#content)

1. **SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing**

    *Tong Zhang, Honglin Lin, Zhou Liu, Chong Chen, Wentao Zhang*

    ACL, 2026. [Published](https://aclanthology.org/2026.acl-long.807/) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

2. **AutoFigure-Edit: Generating Editable Scientific Illustrations via Reference-Guided Styling**

    *Zhen Lin, Qiujie Xie, Minjun Zhu, Shichen Li, Qiyao Sun, Enhao Gu, Yiran Ding, Ke Sun, Fang Guo, Panzhong Lu, Zhiyuan Ning, Yixuan Weng, Yue Zhang*

    ACL System Demonstrations, 2026. [Published](https://aclanthology.org/2026.acl-demo.6/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

3. **EvoDiagram: Agentic Editable Diagram Creation via Design Expertise Evolution**

    *Tianfu Wang, Leilei Ding, Ziyang Tao, Yi Zhan, Zhiyuan Ma, Wei Wu, Yuxuan Lei, Yuan Feng, Junyang Wang, Yin Wu, Yizhao Xu, Hongyuan Zhu, Qi Liu, Nicholas Jing Yuan, Yanyong Zhang, Hui Xiong*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.09568) · `System` · `📦 2D Visual Artifacts`

4. **GenAI-DrawIO-Creator: A Framework for Automated Diagram Generation**

    *Jinze Yu, Dayuan Jiang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.05162) · `System` · `📦 2D Visual Artifacts`

5. **PCBSchemaGen: Reward-Guided LLM Code Synthesis for Printed Circuit Boards (PCB) Schematic Design with Structured Verification**

    *Huanghaohe Zou, Peng Han, Emad Nazerian, Mafu Zhang, Zhicheng Guo, Alex Q. Huang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.00510) · `System` · `📦 2D Visual Artifacts` · `🎯 Engineering Design`

6. **SAGE: Structured Agentic Graph Editing for Software Diagrams**

    *Tyler Sivertsen, Neal Singh, James C. Davis*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.01102) · `System` · `📦 2D Visual Artifacts` · `🎯 Engineering Design`

7. **SciFig: Towards Automating Editable Figure Generation for Scientific Papers**

    *Siyuan Huang, Yifan Zhou, Yutong Gao, Zi Yin, Juyang Bai, Xinxin Liu, Rama Chellappa, Chun Pong Lau, Cheng Peng, Sayan Nag, Shraman Pramanick*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.04390) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

8. **AutoFigure: Generating and Refining Publication-Ready Scientific Illustrations**

    *Minjun Zhu, Zhen Lin, Yixuan Weng, Panzhong Lu, et al.*

    ICLR, 2026. [Published](https://openreview.net/forum?id=5N3z9JQJKq) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

9. **PaperBanana: Automating Academic Illustration for AI Scientists**

    *Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/65206) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

10. **From Pixels to Paths: A Multi-Agent Framework for Editable Scientific Illustration**

    *Jianwen Sun, Fanrui Zhang, Yukang Feng, Chuanhao Li, Zizhen Li, Jiaxin Ai, Yifan Chang, Yu Dai, Kaipeng Zhang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.27452) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

11. **From Words to Structured Visuals: A Benchmark and Framework for Text-to-Diagram Generation and Editing**

    *Jingxuan Wei, Cheng Tan, Qi Chen, Gaowei Wu, et al.*

    CVPR, 2025. [Published](https://openaccess.thecvf.com/content/CVPR2025/html/Wei_From_Words_to_Structured_Visuals_A_Benchmark_and_Framework_for_CVPR_2025_paper.html) · `Benchmark` · `📦 2D Visual Artifacts`

12. **LLM Code Customization with Visual Results: A Benchmark on TikZ**

    *Charly Reux, Mathieu Acher, Djamel Eddine Khelladi, Olivier Barais, Clément Quinton*

    EASE, 2025. [Published](https://doi.org/10.1145/3756681.3757003) · `Benchmark` · `📦 2D Visual Artifacts`

13. **SciSketch: An Open-source Framework for Automated Schematic Diagram Generation in Scientific Papers**

    *Zihang Wang, Yilun Zhao, Kaiyan Zhang, Chen Zhao, Manasi Patwardhan, Arman Cohan*

    EMNLP System Demonstrations, 2025. [Published](https://aclanthology.org/2025.emnlp-demos.28/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

14. **SketchAgent: Generating Structured Diagrams from Hand-Drawn Sketches**

    *Cheng Tan, Qi Chen, Jingxuan Wei, et al.*

    IJCAI, 2025. [Published](https://doi.org/10.24963/ijcai.2025/214) · `System` · `📦 2D Visual Artifacts`

15. **MathemaTikZ: A Dataset and Benchmark for Mathematical Diagram Generation**

    *Rizwaan Malik, Rebecca Li Hao, Ritika Kacholia, Dorottya Demszky*

    Learning @ Scale, 2025. [Published](https://doi.org/10.1145/3698205.3729558) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Educational Support`

### [Visual Documents](#content)

#### [Posters](#content)

1. **AutoPP: Towards Automated Product Poster Generation and Optimization**

    *Jiahao Fan, Yuxin Qin, Wei Feng, Yanyin Chen, et al.*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i5.37377) · `System` · `📦 2D Visual Artifacts` · `🎯 Brand Communication`

2. **PosterForest: Hierarchical Multi-Agent Collaboration for Scientific Poster Generation**

    *Jiho Choi, Seojeong Park, Seongjong Song, Hyunjung Shim*

    ACL, 2026. [Published](https://aclanthology.org/2026.acl-long.15/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

3. **P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark**

    *Tao Sun, Enhao Pan, Zhengkai Yang, Kaixin Sui, Jiajun Shi, Xianfu Cheng, Tongliang Li, Wenhao Huang, Ge Zhang, Jian Yang, Zhoujun Li*

    ICLR, 2026. [Published](https://openreview.net/pdf/9479107515b2f45e615a7b7d5c49fe69d678c264.pdf) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

4. **Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers**

    *Wei Pang, Kevin Qinghong Lin, Xiangru Jian, Xi He, Philip Torr*

    NeurIPS, 2025. [Published](https://openreview.net/forum?id=p0E74lpRBD) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

#### [Presentations](#content)

1. **DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation**

    *Hao Zheng, Guozhao Mo, Xinru Yan, et al.*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.22839) · `System` · `📦 2D Visual Artifacts`

2. **Narrative-Driven Paper-to-Slide Generation via ArcDeck**

    *Tarik Can Ozden, Sachidanand VS, Furkan Horoz, Ozgur Kara, Junho Kim, James Matthew Rehg*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.11969) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

3. **SlidesGen-Bench: Evaluating Slides Generation via Computational and Quantitative Metrics**

    *Yunqiao Yang, Wenbo Li, Houxing Ren, Zimu Lu, Ke Wang, Zhiyuan Huang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.09487) · `Benchmark` · `📦 2D Visual Artifacts`

4. **SlideBot: A Multi-Agent Framework for Generating Informative, Reliable, Multi-Modal Presentations**

    *Eric Xie, Danielle Waterfield, Michael Kennedy, Aidong Zhang*

    EAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i48.42124) · `System` · `📦 2D Visual Artifacts` · `🎯 Educational Support`

5. **DECKBench: Benchmarking Multi-Agent Frameworks for Academic Slide Generation and Editing**

    *Daesik Jang, Morgan Lindsay Heisler, Linzi Xing, Yifei Li, Edward Wang, Ying Xiong, Yong Zhang, Zhenan Fan*

    KDD, 2026. [Published](https://doi.org/10.1145/3770855.3817525) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

6. **Auto-Slides: An Interactive Multi-Agent System for Creating and Customizing Research Presentations**

    *Yuheng Yang, Wenjia Jiang, Yang Wang, Yi Song, Yiwei Wang, Chi Zhang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.11062) · `System` · `📦 2D Visual Artifacts` · `🎯 Educational Support`

7. **SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation**

    *Xin Liang, Xiang Zhang, Yiwei Xu, Siqi Sun, Chenyu You*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.04529) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

8. **PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides**

    *Hao Zheng, Xinyan Guan, Hao Kong, Wenkai Zhang, Jia Zheng, Weixiang Zhou, Hongyu Lin, Yaojie Lu, Xianpei Han, Le Sun*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.728/) · `Benchmark` · `📦 2D Visual Artifacts`

9. **PreGenie: An Agentic Framework for High-quality Visual Presentation Generation**

    *Xiaojie Xu, Xinli Xu, Sirui Chen, Haoyu Chen, Fan Zhang, Ying-Cong Chen*

    Findings of EMNLP, 2025. [Published](https://aclanthology.org/2025.findings-emnlp.165/) · `System` · `📦 2D Visual Artifacts`


## [Audio Artifacts](#content)

1. **Feedback-Driven Retrieval-Augmented Audio Generation with Large Audio Language Models**

    *Junqi Zhao, Chenxing Li, Jinzheng Zhao, Rilin Chen, Dong Yu, Mark D. Plumbley, Wenwu Wang*

    ICASSP, 2026. [Published](https://doi.org/10.1109/ICASSP55912.2026.11462219) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

2. **Orchestrating Audio: Multi-Agent Framework for Long-Video Audio Synthesis**

    *Yehang Zhang, Xinli Xu, Xiaojie Xu, Doudou Zhang, Li Liu, Ying-Cong Chen*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.1133/) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production` · [Code](https://lvas-agent.github.io)

3. **WavCraft: Audio Editing and Generation with Large Language Models**

    *Jinhua Liang, Huan Zhang, Haohe Liu, Yin Cao, Qiuqiang Kong, Xubo Liu, Wenwu Wang, Mark D. Plumbley, Huy Phan, Emmanouil Benetos*

    ICLR Workshop, 2024. [Published](https://openreview.net/forum?id=xJw7x2ZBex) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production` · [Code](https://github.com/JinhuaLiang/WavCraft)

### [Music](#content)

1. **Libretto: Giving LLM Agents a Sense of Musical Structure**

    *Yichen Xu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2606.22708) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

2. **CoComposer: LLM Multi-agent Collaborative Music Composition**

    *Peiwen Xing, Aske Plaat, Niki van Stein*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.00132) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

3. **MusicSwarm: Biologically Inspired Intelligence for Music Composition**

    *Markus J. Buehler*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.11973) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

4. **WeaveMuse: An Open Agentic System for Multimodal Music Understanding and Generation**

    *Emmanouil Karystinaios*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.11183) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

5. **ComposerX: Multi-Agent Symbolic Music Composition with LLMs**

    *Qixin Deng, Qikai Yang, Ruibin Yuan, et al.*

    ISMIR, 2024. [Published](https://doi.org/10.5281/zenodo.14877425) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

### [Spoken Audio](#content)

1. **AI4Reading: Chinese Audiobook Interpretation System Based on Multi-Agent Collaboration**

    *Minjiang Huang, Jipeng Qiang, Yi Zhu, Chaowei Zhang, Xiangyu Zhao, Kui Yu*

    ACL System Demonstrations, 2025. [Published](https://aclanthology.org/2025.acl-demo.21/) · `System` · `📦 Audio Artifacts` · `🎯 Educational Support`


## [Video Artifacts](#content)

### [Expository Videos](#content)

1. **Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation**

    *Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.11790) · `System` · `📦 Video Artifacts` · `🎯 Educational Support`

2. **ManimAgent: Self-Evolving Multimodal Agents for Visual Education**

    *Wenjia Jiang, Zongyuan Cai, Yuanhang Shao, Chenru Wang, Boyan Han, Zhixue Song, Keyu Chen, Shengwei An, Xu Yang, Zhou Yang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2606.30296) · `System` · `📦 Video Artifacts` · `🎯 Educational Support`

3. **Code2Video: A Code-centric Paradigm for Educational Video Creation**

    *Yanzhe Chen, Kevin Qinghong Lin, Mike Zheng Shou*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/65050) · `System` · `📦 Video Artifacts` · `🎯 Educational Support`

4. **Paper2Video: Automatic Video Generation from Scientific Papers**

    *Zeyu Zhu, Kevin Qinghong Lin, Mike Zheng Shou*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.05096) · `System` · `📦 Video Artifacts` · `🎯 Scientific Research`

5. **MapStory: Prototyping Editable Map Animations with LLM Agents**

    *Aditya Gunturu, Ben Pearman, Keiichi Ihara, Morteza Faraji, Bryan Wang, Rubaiat Habib Kazi, Ryo Suzuki*

    UIST, 2025. [Published](https://doi.org/10.1145/3746059.3747664) · `System` · `📦 Video Artifacts` · `🎯 Professional Work`

### [Narrative Videos](#content)

1. **CoMA: Compositional Human Motion Generation with Multi-modal Agents**

    *Shanlin Sun, Jiaqi Xu, Gabriel de Araujo, Shenghan Zhou, Hanwen Zhang, Ziheng Huang, Chenyu You, Xiaohui Xie*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i11.37878) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

2. **FantasyHSI: Video-Generation-Centric 4D Human Synthesis in Any Scene Through a Graph-Based Multi-Agent Framework**

    *Lingzhou Mu, Qiang Wang, Fan Jiang, Mengchao Wang, Mu Xu, Kai Zhang*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i10.37758) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

3. **GENMAC: Compositional Text-to-Video Generation with Multi-Agent Collaboration**

    *Kaiyi Huang, Yukun Huang, Xuefei Ning, Zinan Lin, Yu Wang, Xihui Liu*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i7.37418) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

4. **Authoring for Living Worlds: Tool-Constrained LLM Agents for Executable Multi-Actor Scenarios**

    *Nicolae Cudlenco, Mihai Masala, Marius Leordeanu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.10383) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

5. **BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation**

    *Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2603.02816) · `System` · `📦 Video Artifacts` · `🎯 Brand Communication`

6. **MUSE: A Multi-agent Framework for Unconstrained Story Envisioning via Closed-Loop Cognitive Orchestration**

    *Wenzhang Sun, Zhenyu Wang, Zhangchi Hu, Chunfeng Wang, Hao Li, Wei Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.03028) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

7. **SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation**

    *Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05489) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

8. **VideoMemory: Toward Consistent Video Generation via Memory Integration**

    *Jinsong Zhou, Yihua Du, Xinli Xu, Luozhou Wang, Zijie Zhuang, Yehang Zhang, Shuaibo Li, Xiaojun Hu, Bolan Su, Ying-cong Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.03655) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

9. **HAMLET: A Hierarchical and Adaptive Multi-Agent Framework for Live Embodied Theatrics**

    *Shufan Jiang, Sizhou Chen, Chi Zhang, Xiao-Lei Zhang, Xuelong Li*

    ICLR, 2026. [Published](https://openreview.net/forum?id=MKwW04UHW1) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

10. **AutoMV: An Automatic Multi-Agent System for Music Video Generation**

    *Xiaoxuan Tang, Xinping Lei, Chaoran Zhu, Shiyun Chen, Ruibin Yuan, Yizhi Li, Changjae Oh, Ge Zhang, Wenhao Huang, Emmanouil Benetos, Yang Liu, Jiaheng Liu, Yinghao Ma*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.12196) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

11. **Hollywood Town: Long-Video Generation via Cross-Modal Multi-Agent Orchestration**

    *Zheng Wei, Mingchen Li, Zeqian Zhang, Ruibin Yuan, Pan Hui, Huamin Qu, James Evans, Maneesh Agrawala, Anyi Rao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.22431) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

12. **PersonaVlog: Personalized Multimodal Vlog Generation with Multi-Agent Collaboration and Iterative Self-Correction**

    *Xiaolu Hou, Bing Ma, Jiaxiang Cheng, Xuhua Ren, Kai Yu, Wenyue Li, Tianxiang Zheng, Qinglin Lu*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.13602) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

13. **VISTA: A Test-Time Self-Improving Video Generation Agent**

    *Do Xuan Long, Xingchen Wan, Hootan Nakhost, Chen-Yu Lee, Tomas Pfister, Sercan Ö. Arık*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.15831) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

14. **AniMaker: Multi-Agent Animated Storytelling with MCTS-Driven Clip Generation**

    *Haoyuan Shi, Yunxin Li, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang*

    SIGGRAPH Asia, 2025. [Published](https://doi.org/10.1145/3757377.3764009) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

15. **AniME: Adaptive Multi-Agent Planning for Long Animation Generation**

    *Lisai Zhang, Baohan Xu, Siqian Yang, Mingyu Yin, Jing Liu, Chao Xu, Siqi Wang, Yidi Wu, Yuxin Hong, Zihao Zhang, Yanzhang Liang, Yudong Jiang*

    SIGGRAPH Asia, 2025. [Published](https://doi.org/10.1145/3757374.3771455) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

16. **StoryAgent: Customized Storytelling Video Generation via Multi-Agent Collaboration**

    *Panwen Hu, Jin Jiang, Jianqi Chen, Mingfei Han, Shengcai Liao, Xiaojun Chang, Xiaodan Liang*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2411.04925) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

### [Video Editing and Repair](#content)

1. **GLANCE: A Global-Local Coordination Multi-Agent Framework for Music-Grounded Non-Linear Video Editing**

    *Zihao Lin, Haibo Wang, Zhiyang Xu, Siyao Dai, Huanjie Dong, Xiaohan Wang, Yolo Y. Tang, Yixin Wang, Qifan Wang, Lifu Huang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05076) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

2. **From Shots to Stories: LLM-Assisted Video Editing with Unified Language Representations**

    *Yuzhi Li, Haojun Xu, Feng Tian*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2505.12237) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

3. **UniVA: Universal Video Agent towards Open-Source Next-Generation Video Generalist**

    *Zhengyang Liang, Daoan Zhang, Huichi Zhou, Rui Huang, Bobo Li, Yuechen Zhang, Shengqiong Wu, Xiaohan Wang, Jiebo Luo, Lizi Liao, Hao Fei*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.08521) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

4. **EditDuet: A Multi-Agent System for Video Non-Linear Editing**

    *Marcelo Sandoval-Castañeda, Bryan Russell, Josef Sivic, Gregory Shakhnarovich, Fabian Caba Heilbron*

    SIGGRAPH, 2025. [Published](https://doi.org/10.1145/3721238.3730761) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`


## [Spatial Artifacts](#content)

### [3D Assets](#content)

#### [Visual Assets](#content)

1. **EZBlender: Efficient 3D Editing with Plan-and-ReAct Agent**

    *Hao Wang, Wenhui Zhu, Shao Tang, Zhipeng Wang, Xuanzhao Dong, Xin Li, Xiwen Chen, Ashish Bastola, Xinhao Huang, Yalin Wang, Abolfazl Razi*

    WACV Workshops, 2026. [Published](https://openaccess.thecvf.com/content/WACV2026W/VALED/html/Wang_EZBlender_Efficient_3D_Editing_with_Plan-and-ReAct_Agent_WACVW_2026_paper.html) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

2. **3Dify: a Framework for Procedural 3D-CG Generation Assisted by LLMs Using MCP and RAG**

    *Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Satoshi Ohshima, Takahiro Katagiri*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.04536) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

3. **LL3M: Large Language 3D Modelers**

    *Sining Lu, Guan Chen, Nam Anh Dinh, Itai Lang, Ari Holtzman, Rana Hanocka*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.08228) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

4. **SmartAvatar: Text- and Image-Guided Human Avatar Generation with VLM AI Agents**

    *Alexander Huang-Menders, Xinhang Liu, Andy Xu, Yuyao Zhang, Chi-Keung Tang, Yu-Wing Tai*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2506.04606) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

5. **ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling**

    *Shuyuan Zhang, ChenHan Jiang, Zuoou Li, Jiankang Deng*

    NeurIPS, 2025. [Published](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5e2217482fa75556f1970be809acd3f8-Abstract-Conference.html) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

#### [Parametric Models](#content)

1. **ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation**

    *Yunhan Xu, Qifeng Wu, Xunjin Li, Yuanwei Bin, Qingsong Yao, Jianghang Gu, Guan Wang, Weihao Lv, Huiyu Yang, Wenfa Luo, Jiao Xiang, Yuntian Chen, Shiyi Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.05750) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

2. **TurboAgent: An LLM-Driven Autonomous Multi-Agent Framework for Turbomachinery Aerodynamic Design**

    *Juan Du, Yueteng Wu, Pan Zhao, Yuze Liu, Min Zhang, Xiaobin Xu, Xinglong Zhang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.06747) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

3. **Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek**

    *Xueyang Li, Jiahao Li, Yu Song, Yunzhong Lou, Xiangdong Zhou*

    ICLR, 2026. [Published](https://openreview.net/forum?id=PzIc2TxhwN) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

4. **Debate2Create: Robot Co-design via Multi-Agent LLM Debate**

    *Kevin Qiu, Marek Cygan*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/66635) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

5. **SPADA: A Verifiable Test-Driven Agent for Controllable Parametric CAD Assembly Generation**

    *Keyou Zheng, Xuyang Su, Jiewu Leng*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/62308) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

6. **CADDesigner: Conceptual CAD Model Generation with a General-Purpose Agent**

    *Fengxiao Fan, Jingzhe Ni, Xiaolong Yin, Sirui Wang, Xingyu Lu, Qiang Zou, Ruofeng Tong, Min Tang, Peng Du*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.01031) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

7. **Generative AI for CAD Automation: Leveraging Large Language Models for 3D Modelling**

    *Sumit Kumar, Sarthak Kapoor, Harsh Vardhan, Yao Zhao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.00843) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

8. **MEDA: A Multi-Agent System For Parametric CAD Model Creation**

    *Nirmal Panta, Sakar Kafley, Rabi Acharya, Samridh Parajuli, Dipesh Parajuli, Pradip Panta, Sujan Belbase, Saurab Pant, Amit Regmi, Atsushi Tanaka, Christopher McComb*

    ASME IDETC-CIE, 2025. [Published](https://doi.org/10.1115/DETC2025-163946) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

### [3D Scenes](#content)

#### [Spatial Worlds](#content)

1. **MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction**

    *Ruijie Xu, Xinnan Zhu, Jiayu Ying, Daoguo Dong, Yuzhou Ji, Xin Tan*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2606.14168) · `System` · `📦 Spatial Artifacts`

2. **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI**

    *Hongchi Xia, Xuan Li, Zhaoshuo Li, Qianli Ma, Jiashu Xu, Ming-Yu Liu, Yin Cui, Tsung-Yi Lin, Wei-Chiu Ma, Shenlong Wang, Shuran Song, Fangyin Wei*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.10116) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

3. **StoryBlender: Inter-Shot Consistent and Editable 3D Storyboard with Spatial-temporal Dynamics**

    *Bingliang Li, Zhenhong Sun, Jiaming Bian, Yuehao Wu, Yifu Wang, Hongdong Li, Yatao Bian, Huadong Mo, Daoyi Dong*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.03315) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

4. **Scenethesis: A Language and Vision Agentic Framework for 3D Scene Generation**

    *Lu Ling, Chen-Hsuan Lin, Tsung-Yi Lin, Yifan Ding, Yu Zeng, Yichen Sheng, Yunhao Ge, Ming-Yu Liu, Aniket Bera, Zhaoshuo Li*

    ICLR, 2026. [Published](https://openreview.net/forum?id=SzhezVoaNB) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

5. **Code2Worlds: Empowering Coding LLMs for 4D World Generation**

    *Yi Zhang, Yunshuang Wang, Zeyu Zhang, Hao Tang*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/64546) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

6. **SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes**

    *Nicholas Pfaff, Thomas Cohn, Sergey Zakharov, Rick Cory, Russ Tedrake*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/63465) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

7. **Agentic 3D Scene Generation with Spatially Contextualized VLMs**

    *Xinhang Liu, Yu-Wing Tai, Chi-Keung Tang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2505.20129) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

8. **RAISECity: A Multimodal Agent Framework for Reality-Aligned 3D World Generation at City-Scale**

    *Shengyuan Wang, Zhiheng Zheng, Yu Shang, Lixuan He, Yangcheng Yu, Fan Hangyu, Jie Feng, Qingmin Liao, Yong Li*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.18005) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

9. **RoomPlanner: Explicit Layout Planner for Easier LLM-Driven 3D Room Generation**

    *Wenzhuo Sun, Mingjian Liang, Wenxuan Song, Xuelian Cheng, Zongyuan Ge*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.17048) · `System` · `📦 Spatial Artifacts`

10. **WorldCraft: Photo-Realistic 3D World Creation and Customization via LLM Agents**

    *Xinhang Liu, Chi-Keung Tang, Yu-Wing Tai*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2502.15601) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

#### [Engineered Models](#content)

1. **Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM**

    *Abir Khan Ratul, Sanjay Acharjee, Somin Park, Md Nazmus Sakib*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.20838) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`


## [Behavioral Artifacts](#content)

### [Software Systems](#content)

#### [Software Repositories](#content)

1. **ComfySearch: Autonomous Exploration and Reasoning for ComfyUI Workflows**

    *Jinwei Su, Qizhen Lan, Zeyu Wang, et al.*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.04060) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

2. **CodeCRDT: Observation-Driven Coordination for Multi-Agent LLM Code Generation**

    *Sergey Pugachev*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.18893) · `System` · `📦 Behavioral Artifacts`

3. **Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI Agents**

    *Jiacheng Miao, Joe R. Davis, Yaohui Zhang, Jonathan K. Pritchard, James Zou*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.06917) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

4. **DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation**

    *Ziming You, Yumiao Zhang, Dexuan Xu, Yiwei Lou, Yandong Yan, Wei Wang, Huamin Zhang, Yu Huang*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.58/) · `System` · `📦 Behavioral Artifacts` · `🎯 Professional Work`

5. **CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-Level Coding Challenges**

    *Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, Zhi Jin*

    ACL, 2024. [Published](https://aclanthology.org/2024.acl-long.737/) · `System` · `📦 Behavioral Artifacts`

6. **AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation**

    *Dong Huang, Jie M. Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, Heming Cui*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2312.13010) · `System` · `📦 Behavioral Artifacts`

7. **DrugAgent: Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration**

    *Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Yingzhou Lu, Yue Zhao*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2411.15692) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

#### [Web Applications](#content)

1. **InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training**

    *Ziyun Zhang, Zezhou Wang, Xiaoyi Zhang, Zongyu Guo, Jiahao Li, Bin Li, Yan Lu*

    ACL, 2026. [Published](https://aclanthology.org/2026.acl-long.1313/) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

2. **Demonstrating ViviDoc: Generating Interactive Documents through Human-Agent Collaboration**

    *Yinghao Tang, Yupeng Xie, Yingchaojie Feng, Tingfeng Lan, Wei Chen*

    ACL System Demonstrations, 2026. [Published](https://aclanthology.org/2026.acl-demo.79/) · `System` · `📦 Behavioral Artifacts` · `🎯 Educational Support`

3. **Paper2Web: Let's Make Your Paper Alive!**

    *Yuhang Chen, Tianpeng Lv, Yao Wan, Philip S. Yu, Dongping Chen*

    ACL System Demonstrations, 2026. [Published](https://aclanthology.org/2026.acl-demo.57/) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

4. **Vision-Guided Iterative Refinement for Frontend Code Generation**

    *Hannah Sansford, Derek H. C. Law, Wei Liu, Abhishek Tripathi, Niresh Agarwal, Gerrit J. J. van den Burg*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05839) · `System` · `📦 Behavioral Artifacts`

5. **DuetUI: A Bidirectional Context Loop for Human-Agent Co-Generation of Task-Oriented Interfaces**

    *Yuan Xu, Shaowen Xiang, Yizhi Song, Ruoting Sun, Xin Tong*

    CHI, 2026. [Published](https://dl.acm.org/doi/10.1145/3772318.3790441) · `System` · `📦 Behavioral Artifacts`

6. **DashChat: Interactive Authoring of Performance Dashboard Design Prototypes through Conversation with LLM-Powered Agents**

    *Siqi Shen, Ziyue Lin, Honghui Mei, Wanchen Liu, Chengye Xin, Wenzhuo Dai, Siming Chen, Xiao Wen, Xingyu Lan*

    CHI EA, 2026. [Published](https://dl.acm.org/doi/10.1145/3772363.3798634) · `System` · `📦 Behavioral Artifacts` · `🎯 Professional Work`

7. **Human-Agent Collaborative Paper-to-Page Crafting**

    *Qianli Ma, Siyu Wang, Yilin Chen, Yinhao Tang, Yixiang Yang, Chang Guo, Bingjie Gao, Zhening Xing, Yanan Sun, Zhipeng Zhang*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.1988/) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

8. **WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning**

    *Zimu Lu, Houxing Ren, Yunqiao Yang, Ke Wang, Zhuofan Zong, Junting Pan, Mingjie Zhan, Hongsheng Li*

    ICLR, 2026. [Published](https://openreview.net/forum?id=fE14yWa68Z) · `System` · `📦 Behavioral Artifacts`

9. **AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines**

    *Yifan Wu, Yiran Peng, Yiyu Chen, Jianhao Ruan, Zijie Zhuang, Cheng Yang, Jiayi Zhang, Man Chen, Yenchi Tseng, Zhaoyang Yu, Liang Chen, Yuyao Zhai, Bang Liu, Chenglin Wu, Yuyu Luo*

    ICML, 2026. [Published](https://openreview.net/forum?id=jBPFdqmOck) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

10. **Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification**

    *Zehai He, Wenyi Hong, Zhen Yang, Ziyang Pan, Mingdao Liu, Xiaotao Gu, Jie Tang*

    ICML, 2026. [Published](https://openreview.net/forum?id=lJpXXwhRRF) · `Benchmark` · `📦 Behavioral Artifacts`

11. **Compiling Large Multi-Modal Requirement Documents into Runnable Software Systems: From an Agentic Test-Driven Perspective**

    *Weiyu Kong, Yun Lin, Xiwen Teoh, Duc-Minh Nguyen, Ruofei Ren, Jiaxin Chang, Haoxu Hu, Haoyu Chen*

    ISSTA, 2026. [Published](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) · `System` · `📦 Behavioral Artifacts`

12. **Computer-Use Agents as Judges for Generative User Interface**

    *Kevin Qinghong Lin, Siyuan Hu, Linjie Li, et al.*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.15567) · `System` · `📦 Behavioral Artifacts`

13. **WebVIA: A Web-based Vision-Language Agentic Framework for Interactive and Verifiable UI-to-Code Generation**

    *Mingde Xu, Zhen Yang, Wenyi Hong, et al.*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.06251) · `System` · `📦 Behavioral Artifacts`

#### [Games](#content)

1. **Infinite Worlds with Versatile Interactions**

    *Zelin Gao, Qiuyu Wang, Jiapeng Zhu, Jingye Chen, Zichen Liu, Qingyan Bai, Jiahao Wang, Yufeng Yuan, Hanlin Wang, Yichong Lu, Ka Leong Cheng, Haojie Zhang, Jian Gao, Tianrui Feng, Yuzheng Liu, Yao Yao, Yinghao Xu, Xing Zhu, Yujun Shen, Hao Ouyang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.07534) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production` · [Code](https://github.com/robbyant/lingbot-world-v2)

2. **OpenGame: Open Agentic Coding for Games**

    *Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, Jiaming Han, Tianshuo Peng, Kaixuan Fan, Manyuan Zhang, Xiangyu Yue*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.18394) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

3. **AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems**

    *Lei Yin, Wentao Cheng, Zhida Qin, Tianyu Huang, Yidong Li, Gangyi Ding*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.111/) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

4. **V-GameGym: Visual Game Generation for Code Large Language Models**

    *Wei Zhang, Jian Yang, Renshuai Tao, Linzheng Chai, Shuyue Guo, Jiajun Wu, Xiaoming Chen, Ganqu Cui, Ning Ding, Xander Xu, Hu Wei, Bowen Zhou*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.276/) · `Benchmark` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

5. **90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development**

    *Yuxuan Wan, Runxin Yang, Shuqing Li, Michael R. Lyu*

    FSE, 2026. [Published](https://conf.researchr.org/details/fse-2026/fse-2026-ideas-visions-and-reflections/41/90-Faster-100-Code-Free-MLLM-Driven-Zero-Code-3D-Game-Development) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

6. **ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas**

    *Xinyu Wang, Wenjun Peng, Qi Wu*

    ICSE, 2026. [Published](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/178/ProxyWar-Dynamic-Assessment-of-LLM-Code-Generation-in-Game-Arenas) · `Benchmark` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

7. **Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings**

    *Alexia Jolicoeur-Martineau*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.00632) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

8. **STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game**

    *Eric Zhou, Shreyas Basavatia, Moontashir Siam, Zexin Chen, Mark O. Riedl*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2505.03547) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

### [Simulation Models](#content)

#### [Virtual World Simulators](#content)

1. **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback**

    *Mengkang Hu, Bowei Xia, Yuran Wu, Ailing Yu, Yude Zou, Qiguang Chen, Shijian Wang, Jiarui Jin, Kexin Li, Wenxiang Jiao, Yuan Lu, Ping Luo*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.22336) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

#### [Physical World Models](#content)

1. **Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents**

    *Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.19190) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

2. **Coding Agent Is Good As World Simulator**

    *Hongyu Wang, Jingquan Wang, Bocheng Zou, Radu Serban, Dan Negrut*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2605.14398) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

3. **Perceptual Self-Reflection in Agentic Physics Simulation Code Generation**

    *Prashant Shende, Bradley Camburn*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.12311) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

4. **Sketch2Simulation: Automating Flowsheet Generation via Multi Agent Large Language Models**

    *Abdullah Bahamdan, Emma Pajak, John D. Hedengren, Antonio del Rio Chanona*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2603.24629) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

5. **AgenticTCAD: A LLM-based Multi-Agent Framework for Automated TCAD Code Generation and Device Optimization**

    *Guangxi Fan, Tianliang Ma, Xuguang Sun, Xun Wang, Kain Lu Low, Leilai Shao*

    DATE, 2026. [Published](https://ieeexplore.ieee.org/document/11539536) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

6. **SOCIA-∇: Textual Gradient Meets Multi-Agent Orchestration for Automated Simulator Generation**

    *Yuncheng Hua, Sion Weatherhead, Mehdi Jafari, Hao Xue, Flora D. Salim*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.18551) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`


## [Application-centered View](#content)

This alternate view re-indexes application-classified papers by their use context. Papers classified on both axes therefore appear in both views.

### [Creative Production](#content)

1. **CoMA: Compositional Human Motion Generation with Multi-modal Agents**

    *Shanlin Sun, Jiaqi Xu, Gabriel de Araujo, Shenghan Zhou, Hanwen Zhang, Ziheng Huang, Chenyu You, Xiaohui Xie*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i11.37878) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

2. **FantasyHSI: Video-Generation-Centric 4D Human Synthesis in Any Scene Through a Graph-Based Multi-Agent Framework**

    *Lingzhou Mu, Qiang Wang, Fan Jiang, Mengchao Wang, Mu Xu, Kai Zhang*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i10.37758) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

3. **GENMAC: Compositional Text-to-Video Generation with Multi-Agent Collaboration**

    *Kaiyi Huang, Yukun Huang, Xuefei Ning, Zinan Lin, Yu Wang, Xihui Liu*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i7.37418) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

4. **StoryBox: Collaborative Multi-Agent Simulation for Hybrid Bottom-Up Long-Form Story Generation Using Large Language Models**

    *Zehao Chen, Rong Pan, Haoran Li*

    AAAI, 2026. [Published](https://ojs.aaai.org/index.php/AAAI/article/view/40288) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

5. **Constella: Supporting Storywriters’ Interconnected Character Creation through LLM-Based Multi-Agents**

    *Syemin Park, Soobin Park, Youn-kyung Lim*

    ACM TOCHI, 2026. [Published](https://doi.org/10.1145/3796234) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

6. **Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling**

    *Ruijie Ye, Jiayi Zhang, Zhuoxin Liu, Zihao Zhu, Siyuan Yang, Li Li, Tianfu Fu, Franck Dernoncourt, Yue Zhao, Jiacheng Zhu, Ryan Rossi, Wenhao Chai, Zhengzhong Tu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.09084) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

7. **Authoring for Living Worlds: Tool-Constrained LLM Agents for Executable Multi-Actor Scenarios**

    *Nicolae Cudlenco, Mihai Masala, Marius Leordeanu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.10383) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

8. **CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration**

    *Hairui Zhu, Yiying Yang, Tengjin Weng, Ziyu Lu, Xiao Yao, Xiaoyang Ye, Lin Ma, Wenhao Jiang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.05465) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

9. **ComfySearch: Autonomous Exploration and Reasoning for ComfyUI Workflows**

    *Jinwei Su, Qizhen Lan, Zeyu Wang, et al.*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.04060) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

10. **From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives**

    *Aayush Aluru, Chloe Ho, Muhammad Hammouri, Kerry Luo, Myra Malik, Ryan Lagasse, Arjun Bahuguna, Vasu Sharma*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.00918) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

11. **GLANCE: A Global-Local Coordination Multi-Agent Framework for Music-Grounded Non-Linear Video Editing**

    *Zihao Lin, Haibo Wang, Zhiyang Xu, Siyao Dai, Huanjie Dong, Xiaohan Wang, Yolo Y. Tang, Yixin Wang, Qifan Wang, Lifu Huang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05076) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

12. **Infinite Worlds with Versatile Interactions**

    *Zelin Gao, Qiuyu Wang, Jiapeng Zhu, Jingye Chen, Zichen Liu, Qingyan Bai, Jiahao Wang, Yufeng Yuan, Hanlin Wang, Yichong Lu, Ka Leong Cheng, Haojie Zhang, Jian Gao, Tianrui Feng, Yuzheng Liu, Yao Yao, Yinghao Xu, Xing Zhu, Yujun Shen, Hao Ouyang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.07534) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production` · [Code](https://github.com/robbyant/lingbot-world-v2)

13. **Libretto: Giving LLM Agents a Sense of Musical Structure**

    *Yichen Xu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2606.22708) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

14. **Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Creative Writing**

    *Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.14770) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

15. **MUSE: A Multi-agent Framework for Unconstrained Story Envisioning via Closed-Loop Cognitive Orchestration**

    *Wenzhang Sun, Zhenyu Wang, Zhangchi Hu, Chunfeng Wang, Hao Li, Wei Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.03028) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

16. **OpenGame: Open Agentic Coding for Games**

    *Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, Jiaming Han, Tianshuo Peng, Kaixuan Fan, Manyuan Zhang, Xiangyu Yue*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.18394) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

17. **OpenMic: A Multi-Agent-Based Stand-Up Comedy Generation System**

    *Yuyang Wu, Hanzhong Cao, Jianhao Chen, Yufei Li*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.08288) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

18. **SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation**

    *Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05489) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

19. **StoryBlender: Inter-Shot Consistent and Editable 3D Storyboard with Spatial-temporal Dynamics**

    *Bingliang Li, Zhenhong Sun, Jiaming Bian, Yuehao Wu, Yifu Wang, Hongdong Li, Yatao Bian, Huadong Mo, Daoyi Dong*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.03315) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

20. **VideoMemory: Toward Consistent Video Generation via Memory Integration**

    *Jinsong Zhou, Yihua Du, Xinli Xu, Luozhou Wang, Zijie Zhuang, Yehang Zhang, Shuaibo Li, Xiaojun Hu, Bolan Su, Ying-cong Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.03655) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

21. **Exploring Creator-Centric Methods for LLM-Assisted Interactive Storytelling**

    *Yuelu Li, Siyi Wu, Lujin Zhang, Zhihan Guo, Wenchuan Lu, David Yip*

    CHI, 2026. [Published](https://doi.org/10.1145/3772318.3791362) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

22. **Agentic Retoucher for Text-To-Image Generation**

    *Shaocheng Shen, Jianfeng Liang, Chunlei Cai, Cong Geng, Huiyu Duan, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai*

    CVPR, 2026. [Published](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_Agentic_Retoucher_for_Text-To-Image_Generation_CVPR_2026_paper.html) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

23. **AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Systems**

    *Lei Yin, Wentao Cheng, Zhida Qin, Tianyu Huang, Yidong Li, Gangyi Ding*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.111/) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

24. **V-GameGym: Visual Game Generation for Code Large Language Models**

    *Wei Zhang, Jian Yang, Renshuai Tao, Linzheng Chai, Shuyue Guo, Jiajun Wu, Xiaoming Chen, Ganqu Cui, Ning Ding, Xander Xu, Hu Wei, Bowen Zhou*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.276/) · `Benchmark` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

25. **90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development**

    *Yuxuan Wan, Runxin Yang, Shuqing Li, Michael R. Lyu*

    FSE, 2026. [Published](https://conf.researchr.org/details/fse-2026/fse-2026-ideas-visions-and-reflections/41/90-Faster-100-Code-Free-MLLM-Driven-Zero-Code-3D-Game-Development) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

26. **Feedback-Driven Retrieval-Augmented Audio Generation with Large Audio Language Models**

    *Junqi Zhao, Chenxing Li, Jinzheng Zhao, Rilin Chen, Dong Yu, Mark D. Plumbley, Wenwu Wang*

    ICASSP, 2026. [Published](https://doi.org/10.1109/ICASSP55912.2026.11462219) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

27. **HAMLET: A Hierarchical and Adaptive Multi-Agent Framework for Live Embodied Theatrics**

    *Shufan Jiang, Sizhou Chen, Chi Zhang, Xiao-Lei Zhang, Xuelong Li*

    ICLR, 2026. [Published](https://openreview.net/forum?id=MKwW04UHW1) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

28. **Scenethesis: A Language and Vision Agentic Framework for 3D Scene Generation**

    *Lu Ling, Chen-Hsuan Lin, Tsung-Yi Lin, Yifan Ding, Yu Zeng, Yichen Sheng, Yunhao Ge, Ming-Yu Liu, Aniket Bera, Zhaoshuo Li*

    ICLR, 2026. [Published](https://openreview.net/forum?id=SzhezVoaNB) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

29. **ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas**

    *Xinyu Wang, Wenjun Peng, Qi Wu*

    ICSE, 2026. [Published](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/178/ProxyWar-Dynamic-Assessment-of-LLM-Code-Generation-in-Game-Arenas) · `Benchmark` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

30. **EZBlender: Efficient 3D Editing with Plan-and-ReAct Agent**

    *Hao Wang, Wenhui Zhu, Shao Tang, Zhipeng Wang, Xuanzhao Dong, Xin Li, Xiwen Chen, Ashish Bastola, Xinhao Huang, Yalin Wang, Abolfazl Razi*

    WACV Workshops, 2026. [Published](https://openaccess.thecvf.com/content/WACV2026W/VALED/html/Wang_EZBlender_Efficient_3D_Editing_with_Plan-and-ReAct_Agent_WACVW_2026_paper.html) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

31. **BOOKWORLD: From Novels to Interactive Agent Societies for Story Creation**

    *Yiting Ran, Xintao Wang, Tian Qiu, Jiaqing Liang, Yanghua Xiao, Deqing Yang*

    ACL, 2025. [Published](https://aclanthology.org/2025.acl-long.773/) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

32. **3Dify: a Framework for Procedural 3D-CG Generation Assisted by LLMs Using MCP and RAG**

    *Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Satoshi Ohshima, Takahiro Katagiri*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.04536) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

33. **AnimAgents: Coordinating Multi-Stage Animation Pre-Production with Human-Multi-Agent Collaboration**

    *Wen-Fan Wang, Chien-Ting Lu, Jin Ping Ng, Yi-Ting Chiu, Ting-Ying Lee, Miaosen Wang, Bing-Yu Chen, Xiang 'Anthony' Chen*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.17906) · `System` · `🎯 Creative Production`

34. **AutoMV: An Automatic Multi-Agent System for Music Video Generation**

    *Xiaoxuan Tang, Xinping Lei, Chaoran Zhu, Shiyun Chen, Ruibin Yuan, Yizhi Li, Changjae Oh, Ge Zhang, Wenhao Huang, Emmanouil Benetos, Yang Liu, Jiaheng Liu, Yinghao Ma*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.12196) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

35. **CoComposer: LLM Multi-agent Collaborative Music Composition**

    *Peiwen Xing, Aske Plaat, Niki van Stein*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.00132) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

36. **CreAgentive: An Agent Workflow Driven Multi-Category Creative Generation Engine**

    *Yuyang Cheng, Linyue Cai, Changwei Peng, Yumiao Xu, Rongfang Bie, Yong Zhao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.26461) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

37. **From Shots to Stories: LLM-Assisted Video Editing with Unified Language Representations**

    *Yuzhi Li, Haojun Xu, Feng Tian*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2505.12237) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

38. **GraphicBench: A Planning Benchmark for Graphic Design with Language Agents**

    *Dayeon Ki, Tianyi Zhou, Marine Carpuat, Gang Wu, Puneet Mathur, Viswanathan Swaminathan*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2504.11571) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

39. **Hollywood Town: Long-Video Generation via Cross-Modal Multi-Agent Orchestration**

    *Zheng Wei, Mingchen Li, Zeqian Zhang, Ruibin Yuan, Pan Hui, Huamin Qu, James Evans, Maneesh Agrawala, Anyi Rao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.22431) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

40. **LL3M: Large Language 3D Modelers**

    *Sining Lu, Guan Chen, Nam Anh Dinh, Itai Lang, Ari Holtzman, Rana Hanocka*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.08228) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

41. **Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings**

    *Alexia Jolicoeur-Martineau*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.00632) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

42. **MusicSwarm: Biologically Inspired Intelligence for Music Composition**

    *Markus J. Buehler*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.11973) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

43. **PersonaVlog: Personalized Multimodal Vlog Generation with Multi-Agent Collaboration and Iterative Self-Correction**

    *Xiaolu Hou, Bing Ma, Jiaxiang Cheng, Xuhua Ren, Kai Yu, Wenyue Li, Tianxiang Zheng, Qinglin Lu*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.13602) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

44. **SmartAvatar: Text- and Image-Guided Human Avatar Generation with VLM AI Agents**

    *Alexander Huang-Menders, Xinhang Liu, Andy Xu, Yuyao Zhang, Chi-Keung Tang, Yu-Wing Tai*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2506.04606) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

45. **STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game**

    *Eric Zhou, Shreyas Basavatia, Moontashir Siam, Zexin Chen, Mark O. Riedl*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2505.03547) · `System` · `📦 Behavioral Artifacts` · `🎯 Creative Production`

46. **UniVA: Universal Video Agent towards Open-Source Next-Generation Video Generalist**

    *Zhengyang Liang, Daoan Zhang, Huichi Zhou, Rui Huang, Bobo Li, Yuechen Zhang, Shengqiong Wu, Xiaohan Wang, Jiebo Luo, Lizi Liao, Hao Fei*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.08521) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

47. **VISTA: A Test-Time Self-Improving Video Generation Agent**

    *Do Xuan Long, Xingchen Wan, Hootan Nakhost, Chen-Yu Lee, Tomas Pfister, Sercan Ö. Arık*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.15831) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

48. **WeaveMuse: An Open Agentic System for Multimodal Music Understanding and Generation**

    *Emmanouil Karystinaios*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.11183) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

49. **WorldCraft: Photo-Realistic 3D World Creation and Customization via LLM Agents**

    *Xinhang Liu, Chi-Keung Tang, Yu-Wing Tai*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2502.15601) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

50. **Orchid: A Creative Approach for Authoring LLM-Driven Interactive Narratives**

    *Zhen Wu, Serkan Kumyol, Shing Yin Wong, Xiaozhu Hu, Xin Tong, Tristan Braud*

    C&C, 2025. [Published](https://doi.org/10.1145/3698061.3726906) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

51. **StoryWriter: A Multi-Agent Framework for Long Story Generation**

    *Haotian Xia, Hao Peng, Yunjia Qi, Bin Xu, Juanzi Li, Hou Lei, Xiaozhi Wang*

    CIKM, 2025. [Published](https://doi.org/10.1145/3746252.3761616) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

52. **SketchAgent: Language-Driven Sequential Sketch Generation**

    *Yael Vinker, Tamar Rott Shaham, Kristine Zheng, Alex Zhao, Judith E. Fan, Antonio Torralba*

    CVPR, 2025. [Published](https://doi.org/10.1109/CVPR52734.2025.02175) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

53. **Orchestrating Audio: Multi-Agent Framework for Long-Video Audio Synthesis**

    *Yehang Zhang, Xinli Xu, Xiaojie Xu, Doudou Zhang, Li Liu, Ying-Cong Chen*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.1133/) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production` · [Code](https://lvas-agent.github.io)

54. **T2I-Copilot: A Training-Free Multi-Agent Text-to-Image System for Enhanced Prompt Interpretation and Interactive Generation**

    *Chieh-Yun Chen, Min Shi, Gong Zhang, Humphrey Shi*

    ICCV, 2025. [Published](https://doi.org/10.1109/ICCV51701.2025.01803) · `System` · `📦 2D Visual Artifacts` · `🎯 Creative Production`

55. **Can LLMs Generate Good Stories? Insights and Challenges from a Narrative Planning Perspective**

    *Yi Wang, Max Kreminski*

    IEEE CoG, 2025. [Published](https://doi.org/10.1109/CoG64752.2025.11114137) · `Benchmark` · `📦 Textual Artifacts` · `🎯 Creative Production`

56. **ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling**

    *Shuyuan Zhang, ChenHan Jiang, Zuoou Li, Jiankang Deng*

    NeurIPS, 2025. [Published](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5e2217482fa75556f1970be809acd3f8-Abstract-Conference.html) · `System` · `📦 Spatial Artifacts` · `🎯 Creative Production`

57. **EditDuet: A Multi-Agent System for Video Non-Linear Editing**

    *Marcelo Sandoval-Castañeda, Bryan Russell, Josef Sivic, Gregory Shakhnarovich, Fabian Caba Heilbron*

    SIGGRAPH, 2025. [Published](https://doi.org/10.1145/3721238.3730761) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

58. **AniMaker: Multi-Agent Animated Storytelling with MCTS-Driven Clip Generation**

    *Haoyuan Shi, Yunxin Li, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang*

    SIGGRAPH Asia, 2025. [Published](https://doi.org/10.1145/3757377.3764009) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

59. **AniME: Adaptive Multi-Agent Planning for Long Animation Generation**

    *Lisai Zhang, Baohan Xu, Siqian Yang, Mingyu Yin, Jing Liu, Chao Xu, Siqi Wang, Yidi Wu, Yuxin Hong, Zihao Zhang, Yanzhang Liang, Yudong Jiang*

    SIGGRAPH Asia, 2025. [Published](https://doi.org/10.1145/3757374.3771455) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

60. **StoryAgent: Customized Storytelling Video Generation via Multi-Agent Collaboration**

    *Panwen Hu, Jin Jiang, Jianqi Chen, Mingfei Han, Shengcai Liao, Xiaojun Chang, Xiaodan Liang*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2411.04925) · `System` · `📦 Video Artifacts` · `🎯 Creative Production`

61. **StoryVerse: Towards Co-authoring Dynamic Plot with LLM-based Character Simulation via Narrative Planning**

    *Yi Wang, Qian Zhou, David Ledo*

    FDG, 2024. [Published](https://doi.org/10.1145/3649921.3656987) · `System` · `📦 Textual Artifacts` · `🎯 Creative Production`

62. **WavCraft: Audio Editing and Generation with Large Language Models**

    *Jinhua Liang, Huan Zhang, Haohe Liu, Yin Cao, Qiuqiang Kong, Xubo Liu, Wenwu Wang, Mark D. Plumbley, Huy Phan, Emmanouil Benetos*

    ICLR Workshop, 2024. [Published](https://openreview.net/forum?id=xJw7x2ZBex) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production` · [Code](https://github.com/JinhuaLiang/WavCraft)

63. **ComposerX: Multi-Agent Symbolic Music Composition with LLMs**

    *Qixin Deng, Qikai Yang, Ruibin Yuan, et al.*

    ISMIR, 2024. [Published](https://doi.org/10.5281/zenodo.14877425) · `System` · `📦 Audio Artifacts` · `🎯 Creative Production`

### [Brand Communication](#content)

1. **AutoPP: Towards Automated Product Poster Generation and Optimization**

    *Jiahao Fan, Yuxin Qin, Wei Feng, Yanyin Chen, et al.*

    AAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i5.37377) · `System` · `📦 2D Visual Artifacts` · `🎯 Brand Communication`

2. **BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation**

    *Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2603.02816) · `System` · `📦 Video Artifacts` · `🎯 Brand Communication`

3. **Mirror in the Model: Ad Banner Image Generation via Reflective Multi-LLM and Multi-modal Agents**

    *Zhao Wang, Bowen Chen, Yotaro Shimose, Sota Moriyama, Heng Wang, Shingo Takamatsu*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2507.03326) · `System` · `📦 2D Visual Artifacts` · `🎯 Brand Communication`

4. **BannerAgency: Advertising Banner Design with Multimodal LLM Agents**

    *Heng Wang, Yotaro Shimose, Shingo Takamatsu*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.214/) · `System` · `📦 2D Visual Artifacts` · `🎯 Brand Communication`

5. **MADS: Multi-Agent Dialogue Simulation for Diverse Persuasion Data Generation**

    *Mingjin Li, Yu Liu, Huayi Liu, Xiang Ye, Chao Jiang, Hongguang Zhang, Yu Ruan*

    EMNLP Industry Track, 2025. [Published](https://aclanthology.org/2025.emnlp-industry.26/) · `System` · `📦 Textual Artifacts` · `🎯 Brand Communication`

### [Educational Support](#content)

1. **Demonstrating ViviDoc: Generating Interactive Documents through Human-Agent Collaboration**

    *Yinghao Tang, Yupeng Xie, Yingchaojie Feng, Tingfeng Lan, Wei Chen*

    ACL System Demonstrations, 2026. [Published](https://aclanthology.org/2026.acl-demo.79/) · `System` · `📦 Behavioral Artifacts` · `🎯 Educational Support`

2. **Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation**

    *Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.11790) · `System` · `📦 Video Artifacts` · `🎯 Educational Support`

3. **ManimAgent: Self-Evolving Multimodal Agents for Visual Education**

    *Wenjia Jiang, Zongyuan Cai, Yuanhang Shao, Chenru Wang, Boyan Han, Zhixue Song, Keyu Chen, Shengwei An, Xu Yang, Zhou Yang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2606.30296) · `System` · `📦 Video Artifacts` · `🎯 Educational Support`

4. **SlideBot: A Multi-Agent Framework for Generating Informative, Reliable, Multi-Modal Presentations**

    *Eric Xie, Danielle Waterfield, Michael Kennedy, Aidong Zhang*

    EAAI, 2026. [Published](https://doi.org/10.1609/aaai.v40i48.42124) · `System` · `📦 2D Visual Artifacts` · `🎯 Educational Support`

5. **Code2Video: A Code-centric Paradigm for Educational Video Creation**

    *Yanzhe Chen, Kevin Qinghong Lin, Mike Zheng Shou*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/65050) · `System` · `📦 Video Artifacts` · `🎯 Educational Support`

6. **AI4Reading: Chinese Audiobook Interpretation System Based on Multi-Agent Collaboration**

    *Minjiang Huang, Jipeng Qiang, Yi Zhu, Chaowei Zhang, Xiangyu Zhao, Kui Yu*

    ACL System Demonstrations, 2025. [Published](https://aclanthology.org/2025.acl-demo.21/) · `System` · `📦 Audio Artifacts` · `🎯 Educational Support`

7. **Auto-Slides: An Interactive Multi-Agent System for Creating and Customizing Research Presentations**

    *Yuheng Yang, Wenjia Jiang, Yang Wang, Yi Song, Yiwei Wang, Chi Zhang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.11062) · `System` · `📦 2D Visual Artifacts` · `🎯 Educational Support`

8. **EduAgentQG: A Multi-Agent Workflow Framework for Personalized Question Generation**

    *Rui Jia, Min Zhang, Fengrui Liu, Bo Jiang, Kun Kuang, Zhongxiang Dai*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.11635) · `System` · `📦 Textual Artifacts` · `🎯 Educational Support`

9. **EduPlanner: LLM-Based Multiagent Systems for Customized and Intelligent Instructional Design**

    *Xueqiao Zhang, Chao Zhang, Jianwen Sun, Jun Xiao, Yi Yang, Yawei Luo*

    IEEE TLT, 2025. [Published](https://doi.org/10.1109/TLT.2025.3561332) · `System` · `📦 Textual Artifacts` · `🎯 Educational Support`

10. **MathemaTikZ: A Dataset and Benchmark for Mathematical Diagram Generation**

    *Rizwaan Malik, Rebecca Li Hao, Ritika Kacholia, Dorottya Demszky*

    Learning @ Scale, 2025. [Published](https://doi.org/10.1145/3698205.3729558) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Educational Support`

11. **LLM-powered Multi-agent Framework for Goal-oriented Learning in Intelligent Tutoring System**

    *Tianfu Wang, Yi Zhan, Jianxun Lian, Zhengyu Hu, Nicholas Jing Yuan, Qi Zhang, Xing Xie, Hui Xiong*

    The Web Conference Companion, 2025. [Published](https://doi.org/10.1145/3701716.3715244) · `System` · `📦 Textual Artifacts` · `🎯 Educational Support` · [Code](https://github.com/GeminiLight/gen-mentor)

### [Professional Work](#content)

1. **Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Verification**

    *Yi Yuan, Xuhong Wang, Shanzhe Lei*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.05952) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

2. **DashChat: Interactive Authoring of Performance Dashboard Design Prototypes through Conversation with LLM-Powered Agents**

    *Siqi Shen, Ziyue Lin, Honghui Mei, Wanchen Liu, Chengye Xin, Wenzhuo Dai, Siming Chen, Xiao Wen, Xingyu Lan*

    CHI EA, 2026. [Published](https://dl.acm.org/doi/10.1145/3772363.3798634) · `System` · `📦 Behavioral Artifacts` · `🎯 Professional Work`

3. **Benchmarking Agentic Newswriting via Journalistic Workflows**

    *Yen-Che Chien, Kuang-Da Wang, Wei-Yao Wang, Wen-Chih Peng*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.1816/) · `Benchmark` · `📦 Textual Artifacts` · `🎯 Professional Work` · [Code](https://github.com/wywyWang/CoachAI-Projects)

4. **MultiVis-Agent: A Multi-Agent Framework with Logic Rules for Reliable and Comprehensive Cross-Modal Data Visualization**

    *Jinwei Lu, Yuanfeng Song, Chen Zhang, Raymond Chi-Wing Wong*

    PACMMOD (SIGMOD), 2026. [Published](https://doi.org/10.1145/3786670) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

5. **A2P-Vis: an Analyzer-to-Presenter Agentic Pipeline for Visual Insights Generation and Reporting**

    *Shuyu Gan, Renxiang Wang, James Mooney, Dongyeop Kang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.22101) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

6. **CoDA: Agentic Systems for Collaborative Data Visualization**

    *Zichen Chen, Jiefeng Chen, Sercan Ö. Arık, Misha Sra, Tomas Pfister, Jinsung Yoon*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.03194) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

7. **PAME-AI: Patient Messaging Creation and Optimization using Agentic AI**

    *Junjie Luo, Yihong Guo, Anqi Liu, Ritu Agarwal, Gordon Gao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.24263) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

8. **Jupybara: Operationalizing a Design Space for Actionable Data Analysis and Storytelling with LLMs**

    *Huichen Will Wang, Larry Birnbaum, Vidya Setlur*

    CHI, 2025. [Published](https://doi.org/10.1145/3706598.3713913) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

9. **AI-Press: A Multi-Agent News Generating and Feedback Simulation System Powered by Large Language Models**

    *Xiawei Liu, Shiyue Yang, Xinnong Zhang, Haoyu Kuang, Libo Sun, Yihang Yang, Siming Chen, Xuanjing Huang, Zhongyu Wei*

    COLING, 2025. [Published](https://aclanthology.org/2025.coling-demos.8/) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

10. **DatawiseAgent: A Notebook-Centric LLM Agent Framework for Adaptive and Robust Data Science Automation**

    *Ziming You, Yumiao Zhang, Dexuan Xu, Yiwei Lou, Yandong Yan, Wei Wang, Huamin Zhang, Yu Huang*

    EMNLP, 2025. [Published](https://aclanthology.org/2025.emnlp-main.58/) · `System` · `📦 Behavioral Artifacts` · `🎯 Professional Work`

11. **DataWink: Reusing and Adapting SVG-based Visualization Examples with Large Multimodal Models**

    *Liwenhan Xie, Yanna Lin, Can Liu, Huamin Qu, Xinhuan Shu*

    IEEE TVCG, 2025. [Published](https://doi.org/10.1109/TVCG.2025.3634635) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

12. **MapStory: Prototyping Editable Map Animations with LLM Agents**

    *Aditya Gunturu, Ben Pearman, Keiichi Ihara, Morteza Faraji, Bryan Wang, Rubaiat Habib Kazi, Ryo Suzuki*

    UIST, 2025. [Published](https://doi.org/10.1145/3746059.3747664) · `System` · `📦 Video Artifacts` · `🎯 Professional Work`

13. **LightVA: Lightweight Visual Analytics With LLM Agent-Based Task Planning and Execution**

    *Yuheng Zhao, Junjie Wang, Linbin Xiang, Xiaowen Zhang, Zifei Guo, Cagatay Turkay, Yu Zhang, Siming Chen*

    IEEE TVCG, 2024. [Published](https://doi.org/10.1109/TVCG.2024.3496112) · `System` · `📦 2D Visual Artifacts` · `🎯 Professional Work`

14. **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models**

    *Shao, Yijia, Jiang, Yucheng, Kanell, Theodore A., Xu, Peter, Khattab, Omar, Lam, Monica S.*

    NAACL, 2024. [Published](https://aclanthology.org/2024.naacl-long.347/) · `System` · `📦 Textual Artifacts` · `🎯 Professional Work`

### [Scientific Research](#content)

1. **PosterForest: Hierarchical Multi-Agent Collaboration for Scientific Poster Generation**

    *Jiho Choi, Seojeong Park, Seongjong Song, Hyunjung Shim*

    ACL, 2026. [Published](https://aclanthology.org/2026.acl-long.15/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

2. **SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing**

    *Tong Zhang, Honglin Lin, Zhou Liu, Chong Chen, Wentao Zhang*

    ACL, 2026. [Published](https://aclanthology.org/2026.acl-long.807/) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

3. **AutoFigure-Edit: Generating Editable Scientific Illustrations via Reference-Guided Styling**

    *Zhen Lin, Qiujie Xie, Minjun Zhu, Shichen Li, Qiyao Sun, Enhao Gu, Yiran Ding, Ke Sun, Fang Guo, Panzhong Lu, Zhiyuan Ning, Yixuan Weng, Yue Zhang*

    ACL System Demonstrations, 2026. [Published](https://aclanthology.org/2026.acl-demo.6/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

4. **Paper2Web: Let's Make Your Paper Alive!**

    *Yuhang Chen, Tianpeng Lv, Yao Wan, Philip S. Yu, Dongping Chen*

    ACL System Demonstrations, 2026. [Published](https://aclanthology.org/2026.acl-demo.57/) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

5. **A Multi-Agent Human-LLM Collaborative Framework for Closed-Loop Scientific Discovery**

    *Maxwell J. Jacobson, Daniel Xie, Jackson Shen, Adil Wazeer et al.*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.01452) · `System` · `🎯 Scientific Research`

6. **Autonomous Laboratory Agent via Customized Domain-Specific Language Model and Modular AI Interface**

    *Zhuo Diao, Kouma Matsumoto, Linfeng Hou, Hayato Yamashita, Masayuki Abe*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.20669) · `System` · `🎯 Scientific Research`

7. **ChemCRAFT: Agentic Reinforcement Learning for Chemical Language Models for Molecular Design and Synthesis**

    *Hao Li, He Cao, Shenyao Peng, et al.*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.17687) · `System` · `🎯 Scientific Research` · [Code](https://github.com/HowardLi1984/ChemCraft)

8. **DIAGPaper: Diagnosing Valid and Specific Weaknesses in Scientific Papers via Multi-Agent Reasoning**

    *Zhuoyang Zou, Abolfazl Ansari, Delvin Ce Zhang, Dongwon Lee, Wenpeng Yin*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.07611) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

9. **Narrative-Driven Paper-to-Slide Generation via ArcDeck**

    *Tarik Can Ozden, Sachidanand VS, Furkan Horoz, Ozgur Kara, Junho Kim, James Matthew Rehg*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.11969) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

10. **ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog**

    *Lingao Xiao, Yalun Dai, Yangyu Huang, Qihao Zhao, Wenshan Wu, Hugo He, Ruishuo Chen, Jin Jiang, Qianli Ma, Jiahuan Zhang, Xin Zhang, Ying Xin, Yang Ou, Yan Xia, Scarlett Li, Longbo Huang, Zhipeng Zhang, Yang He, Yap Kim Hui, Yan Lu*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.04438) · `System` · `🎯 Scientific Research`

11. **SciFig: Towards Automating Editable Figure Generation for Scientific Papers**

    *Siyuan Huang, Yifan Zhou, Yutong Gao, Zi Yin, Juyang Bai, Xinxin Liu, Rama Chellappa, Chun Pong Lau, Cheng Peng, Sayan Nag, Shraman Pramanick*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2601.04390) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

12. **Human-Agent Collaborative Paper-to-Page Crafting**

    *Qianli Ma, Siyu Wang, Yilin Chen, Yinhao Tang, Yixiang Yang, Chang Guo, Bingjie Gao, Zhening Xing, Yanan Sun, Zhipeng Zhang*

    Findings of ACL, 2026. [Published](https://aclanthology.org/2026.findings-acl.1988/) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

13. **AutoFigure: Generating and Refining Publication-Ready Scientific Illustrations**

    *Minjun Zhu, Zhen Lin, Yixuan Weng, Panzhong Lu, et al.*

    ICLR, 2026. [Published](https://openreview.net/forum?id=5N3z9JQJKq) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

14. **P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark**

    *Tao Sun, Enhao Pan, Zhengkai Yang, Kaixin Sui, Jiajun Shi, Xianfu Cheng, Tongliang Li, Wenhao Huang, Ge Zhang, Jian Yang, Zhoujun Li*

    ICLR, 2026. [Published](https://openreview.net/pdf/9479107515b2f45e615a7b7d5c49fe69d678c264.pdf) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

15. **PaperBanana: Automating Academic Illustration for AI Scientists**

    *Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/65206) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

16. **DECKBench: Benchmarking Multi-Agent Frameworks for Academic Slide Generation and Editing**

    *Daesik Jang, Morgan Lindsay Heisler, Linzi Xing, Yifei Li, Edward Wang, Ying Xiong, Yong Zhang, Zhenan Fan*

    KDD, 2026. [Published](https://doi.org/10.1145/3770855.3817525) · `Benchmark` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

17. **PaperDebugger: A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing**

    *Junyi Hou, Andre Lin Huikai, Nuo Chen, Yiwei Gong, Bingsheng He*

    The Web Conference Companion, 2026. [Published](https://doi.org/10.1145/3774905.3793122) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

18. **Can LLMs Identify Critical Limitations within Scientific Research? A Systematic Evaluation on AI Research Papers**

    *Zhijian Xu, Yilun Zhao, Manasi Patwardhan, Lovekesh Vig, Arman Cohan*

    ACL, 2025. [Published](https://aclanthology.org/2025.acl-long.1009/) · `Benchmark` · `📦 Textual Artifacts` · `🎯 Scientific Research`

19. **From Pixels to Paths: A Multi-Agent Framework for Editable Scientific Illustration**

    *Jianwen Sun, Fanrui Zhang, Yukang Feng, Chuanhao Li, Zizhen Li, Jiaxin Ai, Yifan Chang, Yu Dai, Kaipeng Zhang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.27452) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

20. **Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI Agents**

    *Jiacheng Miao, Joe R. Davis, Yaohui Zhang, Jonathan K. Pritchard, James Zou*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2509.06917) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

21. **Paper2Video: Automatic Video Generation from Scientific Papers**

    *Zeyu Zhu, Kevin Qinghong Lin, Mike Zheng Shou*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.05096) · `System` · `📦 Video Artifacts` · `🎯 Scientific Research`

22. **SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation**

    *Xin Liang, Xiang Zhang, Yiwei Xu, Siqi Sun, Chenyu You*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.04529) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

23. **Queryome: Orchestrating Retrieval, Reasoning, and Synthesis across Biomedical Literature**

    *Pranav Punuru, Nabil Ibtehaz, Swagarika Jaharlal Giri, Harsha Srirangam, Emilia A Tugolukova, Daisuke Kihara*

    bioRxiv, 2025. [Preprint](https://doi.org/10.64898/2025.12.22.696019) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

24. **IdeaSynth: Iterative Research Idea Development Through Evolving and Composing Idea Facets with Literature-Grounded Feedback**

    *Kevin Pu, K. J. Kevin Feng, Tovi Grossman, Tom Hope, Bhavana Dalvi Mishra, Matt Latzke, Jonathan Bragg, Joseph Chee Chang, Pao Siangliulue*

    CHI, 2025. [Published](https://doi.org/10.1145/3706598.3714057) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

25. **SciSketch: An Open-source Framework for Automated Schematic Diagram Generation in Scientific Papers**

    *Zihang Wang, Yilun Zhao, Kaiyan Zhang, Chen Zhao, Manasi Patwardhan, Arman Cohan*

    EMNLP System Demonstrations, 2025. [Published](https://aclanthology.org/2025.emnlp-demos.28/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

26. **Agent Laboratory: Using LLM Agents as Research Assistants**

    *Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum*

    Findings of EMNLP, 2025. [Published](https://aclanthology.org/2025.findings-emnlp.320/) · `System` · `🎯 Scientific Research`

27. **ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models**

    *Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, Sung Ju Hwang*

    NAACL, 2025. [Published](https://aclanthology.org/2025.naacl-long.342/) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

28. **Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers**

    *Wei Pang, Kevin Qinghong Lin, Xiangru Jian, Xi He, Philip Torr*

    NeurIPS, 2025. [Published](https://openreview.net/forum?id=p0E74lpRBD) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

29. **PlotGen: Multi-Agent LLM-based Scientific Data Visualization via Multimodal Retrieval Feedback**

    *Kanika Goswami, Puneet Mathur, Ryan Rossi, Franck Dernoncourt*

    The Web Conference Companion, 2025. [Published](https://doi.org/10.1145/3701716.3716888) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

30. **DrugAgent: Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration**

    *Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Yingzhou Lu, Yue Zhao*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2411.15692) · `System` · `📦 Behavioral Artifacts` · `🎯 Scientific Research`

31. **MARG: Multi-Agent Review Generation for Scientific Papers**

    *Mike D'Arcy, Tom Hope, Larry Birnbaum, Doug Downey*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2401.04259) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

32. **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery**

    *Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha*

    arXiv, 2024. [Preprint](https://arxiv.org/abs/2408.06292) · `System` · `📦 Textual Artifacts` · `🎯 Scientific Research`

33. **ProtAgents: Protein Discovery via Large Language Model Multi-Agent Collaborations Combining Physics and Machine Learning**

    *Alireza Ghafarollahi, Markus J. Buehler*

    Digital Discovery, 2024. [Published](https://doi.org/10.1039/D4DD00013G) · `System` · `🎯 Scientific Research` · [Code](https://github.com/lamm-mit/ProtAgents)

34. **MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization**

    *Zhiyu Yang, Zihan Zhou, Shuo Wang, Xin Cong, Xu Han, Yukun Yan, Zhenghao Liu, Zhixing Tan, Pengyuan Liu, Dong Yu, Zhiyuan Liu, Xiaodong Shi, Maosong Sun*

    Findings of ACL, 2024. [Published](https://aclanthology.org/2024.findings-acl.701/) · `System` · `📦 2D Visual Artifacts` · `🎯 Scientific Research`

### [Engineering Design](#content)

1. **InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training**

    *Ziyun Zhang, Zezhou Wang, Xiaoyi Zhang, Zongyu Guo, Jiahao Li, Bin Li, Yan Lu*

    ACL, 2026. [Published](https://aclanthology.org/2026.acl-long.1313/) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

2. **Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents**

    *Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.19190) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

3. **ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation**

    *Yunhan Xu, Qifeng Wu, Xunjin Li, Yuanwei Bin, Qingsong Yao, Jianghang Gu, Guan Wang, Weihao Lv, Huiyu Yang, Wenfa Luo, Jiao Xiang, Yuntian Chen, Shiyi Chen*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.05750) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

4. **Coding Agent Is Good As World Simulator**

    *Hongyu Wang, Jingquan Wang, Bocheng Zou, Radu Serban, Dan Negrut*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2605.14398) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

5. **PCBSchemaGen: Reward-Guided LLM Code Synthesis for Printed Circuit Boards (PCB) Schematic Design with Structured Verification**

    *Huanghaohe Zou, Peng Han, Emad Nazerian, Mafu Zhang, Zhicheng Guo, Alex Q. Huang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.00510) · `System` · `📦 2D Visual Artifacts` · `🎯 Engineering Design`

6. **Perceptual Self-Reflection in Agentic Physics Simulation Code Generation**

    *Prashant Shende, Bradley Camburn*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.12311) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

7. **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI**

    *Hongchi Xia, Xuan Li, Zhaoshuo Li, Qianli Ma, Jiashu Xu, Ming-Yu Liu, Yin Cui, Tsung-Yi Lin, Wei-Chiu Ma, Shenlong Wang, Shuran Song, Fangyin Wei*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2602.10116) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

8. **SAGE: Structured Agentic Graph Editing for Software Diagrams**

    *Tyler Sivertsen, Neal Singh, James C. Davis*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2607.01102) · `System` · `📦 2D Visual Artifacts` · `🎯 Engineering Design`

9. **Sketch2Simulation: Automating Flowsheet Generation via Multi Agent Large Language Models**

    *Abdullah Bahamdan, Emma Pajak, John D. Hedengren, Antonio del Rio Chanona*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2603.24629) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

10. **TurboAgent: An LLM-Driven Autonomous Multi-Agent Framework for Turbomachinery Aerodynamic Design**

    *Juan Du, Yueteng Wu, Pan Zhao, Yuze Liu, Min Zhang, Xiaobin Xu, Xinglong Zhang*

    arXiv, 2026. [Preprint](https://arxiv.org/abs/2604.06747) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

11. **AgenticTCAD: A LLM-based Multi-Agent Framework for Automated TCAD Code Generation and Device Optimization**

    *Guangxi Fan, Tianliang Ma, Xuguang Sun, Xun Wang, Kain Lu Low, Leilai Shao*

    DATE, 2026. [Published](https://ieeexplore.ieee.org/document/11539536) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

12. **Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek**

    *Xueyang Li, Jiahao Li, Yu Song, Yunzhong Lou, Xiangdong Zhou*

    ICLR, 2026. [Published](https://openreview.net/forum?id=PzIc2TxhwN) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

13. **AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines**

    *Yifan Wu, Yiran Peng, Yiyu Chen, Jianhao Ruan, Zijie Zhuang, Cheng Yang, Jiayi Zhang, Man Chen, Yenchi Tseng, Zhaoyang Yu, Liang Chen, Yuyao Zhai, Bang Liu, Chenglin Wu, Yuyu Luo*

    ICML, 2026. [Published](https://openreview.net/forum?id=jBPFdqmOck) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

14. **Code2Worlds: Empowering Coding LLMs for 4D World Generation**

    *Yi Zhang, Yunshuang Wang, Zeyu Zhang, Hao Tang*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/64546) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

15. **Debate2Create: Robot Co-design via Multi-Agent LLM Debate**

    *Kevin Qiu, Marek Cygan*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/66635) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

16. **SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes**

    *Nicholas Pfaff, Thomas Cohn, Sergey Zakharov, Rick Cory, Russ Tedrake*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/63465) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

17. **SPADA: A Verifiable Test-Driven Agent for Controllable Parametric CAD Assembly Generation**

    *Keyou Zheng, Xuyang Su, Jiewu Leng*

    ICML, 2026. [Published](https://icml.cc/virtual/2026/poster/62308) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

18. **DocAgent: A Multi-Agent System for Automated Code Documentation Generation**

    *Dayu Yang, Antoine Simoulin, Xin Qian, Xiaoyi Liu, Yuwei Cao, Zhaopu Teng, Grey Yang*

    ACL, 2025. [Published](https://aclanthology.org/2025.acl-demo.44/) · `System` · `📦 Textual Artifacts` · `🎯 Engineering Design`

19. **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback**

    *Mengkang Hu, Bowei Xia, Yuran Wu, Ailing Yu, Yude Zou, Qiguang Chen, Shijian Wang, Jiarui Jin, Kexin Li, Wenxiang Jiao, Yuan Lu, Ping Luo*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2512.22336) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

20. **Agentic 3D Scene Generation with Spatially Contextualized VLMs**

    *Xinhang Liu, Yu-Wing Tai, Chi-Keung Tang*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2505.20129) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

21. **CADDesigner: Conceptual CAD Model Generation with a General-Purpose Agent**

    *Fengxiao Fan, Jingzhe Ni, Xiaolong Yin, Sirui Wang, Xingyu Lu, Qiang Zou, Ruofeng Tong, Min Tang, Peng Du*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.01031) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

22. **Generative AI for CAD Automation: Leveraging Large Language Models for 3D Modelling**

    *Sumit Kumar, Sarthak Kapoor, Harsh Vardhan, Yao Zhao*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2508.00843) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

23. **RAISECity: A Multimodal Agent Framework for Reality-Aligned 3D World Generation at City-Scale**

    *Shengyuan Wang, Zhiheng Zheng, Yu Shang, Lixuan He, Yangcheng Yu, Fan Hangyu, Jie Feng, Qingmin Liao, Yong Li*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2511.18005) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

24. **Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM**

    *Abir Khan Ratul, Sanjay Acharjee, Somin Park, Md Nazmus Sakib*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.20838) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

25. **SOCIA-∇: Textual Gradient Meets Multi-Agent Orchestration for Automated Simulator Generation**

    *Yuncheng Hua, Sion Weatherhead, Mehdi Jafari, Hao Xue, Flora D. Salim*

    arXiv, 2025. [Preprint](https://arxiv.org/abs/2510.18551) · `System` · `📦 Behavioral Artifacts` · `🎯 Engineering Design`

26. **MEDA: A Multi-Agent System For Parametric CAD Model Creation**

    *Nirmal Panta, Sakar Kafley, Rabi Acharya, Samridh Parajuli, Dipesh Parajuli, Pradip Panta, Sujan Belbase, Saurab Pant, Amit Regmi, Atsushi Tanaka, Christopher McComb*

    ASME IDETC-CIE, 2025. [Published](https://doi.org/10.1115/DETC2025-163946) · `System` · `📦 Spatial Artifacts` · `🎯 Engineering Design`

<div align="center">
  <h1>Awesome Agentic Artifact Creation</h1>
  <p>
    A curated list of papers on agentic systems that plan, generate, inspect,
    revise, and maintain artifacts.
  </p>
</div>

---

This catalog organizes work by the artifact being constructed rather than by
application domain, workflow stage, or evaluation setup. It accompanies the
[Agentic Artifact Creation survey](https://github.com/GeminiLight/agentic-creation-survey)
and follows the survey's artifact-centered landscape.

The initial release re-audits the survey's candidate systems and benchmarks
against an operational agentic-construction rule. The public list contains only
accepted entries; pending and excluded decisions remain visible in
[`data/audit.csv`](data/audit.csv) and the [audit protocol](AUDIT.md).

## Catalog at a glance

- **144 included papers** spanning **2024–2026**.
- **133 artifact systems** and **11 artifact benchmarks**.
- **156 audited candidates**: 7 pending full-text review and 5 excluded.
- **6 artifact families** and **21 artifact subtypes**.

*Sources: `data/audit.csv` and generated `data/papers.csv`.*

> [!NOTE]
> Counts describe this audited catalog rather than total field output. The audit
> is a structured first pass, and 2026 is an incomplete publication year.

## Scope

- **Text and document artifacts:** creative writing, professional documents,
  reports, and scholarly writing.
- **2D visual artifacts:** data visualizations, diagrams, images, posters, and
  presentations.
- **Music and audio artifacts:** music composition and produced or spoken audio.
- **Video and animation artifacts:** expository, narrative, personalized,
  editing, and animation workflows.
- **3D and spatial artifacts:** objects, scenes, worlds, CAD, and engineering
  geometry.
- **Software and executable artifacts:** repositories, applications, websites,
  user interfaces, games, and simulations.

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before
adding or reclassifying a paper.

## Content

<table>
<tr><th colspan="2">Artifact-centered catalog</th></tr>
<tr><td colspan="2"><strong><a href="#text-and-document-artifacts">1. Text and Document Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#creative-and-narrative-writing">1.1. Creative and Narrative Writing</a></td>
<td>&emsp;<a href="#professional-and-functional-documents">1.2. Professional and Functional Documents</a></td>
</tr>
<tr>
<td>&emsp;<a href="#reports-and-research-writing">1.3. Reports and Research Writing</a></td>
<td></td>
</tr>
<tr><td colspan="2"><strong><a href="#2d-visual-artifacts">2. 2D Visual Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#data-visualization">2.1. Data Visualization</a></td>
<td>&emsp;<a href="#figures-diagrams-and-schematics">2.2. Figures, Diagrams, and Schematics</a></td>
</tr>
<tr>
<td>&emsp;<a href="#images-and-graphic-design">2.3. Images and Graphic Design</a></td>
<td>&emsp;<a href="#posters">2.4. Posters</a></td>
</tr>
<tr>
<td>&emsp;<a href="#presentations">2.5. Presentations</a></td>
<td></td>
</tr>
<tr><td colspan="2"><strong><a href="#music-and-audio-artifacts">3. Music and Audio Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#music-composition">3.1. Music Composition</a></td>
<td>&emsp;<a href="#produced-and-spoken-audio">3.2. Produced and Spoken Audio</a></td>
</tr>
<tr><td colspan="2"><strong><a href="#video-and-animation-artifacts">4. Video and Animation Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#explainer-and-presentation-video">4.1. Explainer and Presentation Video</a></td>
<td>&emsp;<a href="#narrative-and-cinematic-video">4.2. Narrative and Cinematic Video</a></td>
</tr>
<tr>
<td>&emsp;<a href="#personalized-and-branded-video">4.3. Personalized and Branded Video</a></td>
<td>&emsp;<a href="#video-editing-and-refinement">4.4. Video Editing and Refinement</a></td>
</tr>
<tr>
<td>&emsp;<a href="#animation">4.5. Animation</a></td>
<td></td>
</tr>
<tr><td colspan="2"><strong><a href="#3d-and-spatial-artifacts">5. 3D and Spatial Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#3d-objects-and-assets">5.1. 3D Objects and Assets</a></td>
<td>&emsp;<a href="#3d-scenes-and-worlds">5.2. 3D Scenes and Worlds</a></td>
</tr>
<tr>
<td>&emsp;<a href="#cad-and-engineering-geometry">5.3. CAD and Engineering Geometry</a></td>
<td></td>
</tr>
<tr><td colspan="2"><strong><a href="#software-and-executable-artifacts">6. Software and Executable Artifacts</a></strong></td></tr>
<tr>
<td>&emsp;<a href="#applications-and-code-repositories">6.1. Applications and Code Repositories</a></td>
<td>&emsp;<a href="#websites-and-user-interfaces">6.2. Websites and User Interfaces</a></td>
</tr>
<tr>
<td>&emsp;<a href="#games-and-simulations">6.3. Games and Simulations</a></td>
<td></td>
</tr>
</table>

## [Text and Document Artifacts](#content)

### [Creative and Narrative Writing](#content)

1. **From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives**

    *Aayush Aluru, Chloe Ho, Muhammad Hammouri, Kerry Luo, Myra Malik, Ryan Lagasse, Arjun Bahuguna, Vasu Sharma*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2607.00918) · `system`

2. **Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Creative Writing**

    *Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.14770) · `system`

3. **OpenMic: A Multi-Agent-Based Stand-Up Comedy Generation System**

    *Yuyang Wu, Hanzhong Cao, Jianhao Chen, Yufei Li*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.08288) · `system`

4. **Constella: Supporting Storywriters' Interconnected Character Creation through LLM-based Multi-Agents**

    *Syemin Park, Soobin Park, Youn-kyung Lim*

    ACM TOCHI, 2025. [`published`](https://arxiv.org/abs/2507.05820) · `system`

5. **BookWorld: From Novels to Interactive Agent Societies for Creative Story Generation**

    *Yiting Ran, Xintao Wang, Tian Qiu, Jiaqing Liang, Yanghua Xiao, Deqing Yang*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2504.14538) · `system`

6. **CreAgentive: An Agent Workflow Driven Multi-Category Creative Generation Engine**

    *Yuyang Cheng, Linyue Cai, Changwei Peng, Yumiao Xu, Rongfang Bie, Yong Zhao*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.26461) · `system`

7. **StoryBox: Collaborative Multi-Agent Simulation for Hybrid Bottom-Up Long-Form Story Generation**

    *Zehao Chen, Rong Pan, Haoran Li*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.11618) · `system`

8. **StoryWriter: A Multi-Agent Framework for Long Story Generation**

    *Haotian Xia, Hao Peng, Yunjia Qi, Xiaozhi Wang, Bin Xu, Lei Hou, Juanzi Li*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2506.16445) · `system`

9. **StoryVerse: Towards Co-authoring Dynamic Plot with LLM-based Character Simulation via Narrative Planning**

    *Yi Wang, Qian Zhou, David Ledo*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2405.13042) · `system`

### [Professional and Functional Documents](#content)

1. **DocAgent: A Multi-Agent System for Automated Code Documentation Generation**

    *Dayu Yang, Antoine Simoulin, Xin Qian, et al.*

    ACL, 2025. [`published`](https://arxiv.org/abs/2504.08725) · `system`

2. **AgentCTG: Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation**

    *Xinxu Zhou, Jiaqi Bai, Zhenqi Sun, Fanxiang Zeng, Yue Liu*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.13677) · `system`

3. **EduPlanner: LLM-Based Multi-Agent Systems for Customized and Adaptive Instructional Design**

    *Xueqiao Zhang, Chao Zhang, Jianwen Sun, Jun Xiao, Yi Yang, Yawei Luo*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2504.05370) · `system`

4. **MADS: Multi-Agent Dialogue Simulation for Diverse Persuasion**

    *Mingjin Li, Yu Liu, Huayi Liu, Xiang Ye, Chao Jiang, Hongguang Zhang, Yu Ruan*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.05124) · `system`

5. **PAME-AI: Patient Messaging Creation and Optimization using Agentic AI**

    *Junjie Luo, Yihong Guo, Anqi Liu, Ritu Agarwal, Gordon Gao*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.24263) · `system`

6. **Translation Agent: Agentic Translation Using Reflection Workflow**

    *Andrew Ng, Joaquin Dominguez, Nedelina Teneva, John Santerre*

    GitHub, 2024. [`project`](https://github.com/andrewyng/translation-agent) · `system`

### [Reports and Research Writing](#content)

1. **DIAGPaper: Diagnosing Valid and Specific Weaknesses in Scientific Papers via Multi-Agent Reasoning**

    *Zhuoyang Zou, Abolfazl Ansari, Delvin Ce Zhang, Dongwon Lee, Wenpeng Yin*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.07611) · `system`

2. **Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Verification**

    *Yi Yuan, Xuhong Wang, Shanzhe Lei*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.05952) · `system`

3. **PaperDebugger: A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing**

    *Junyi Hou, Andre Lin Huikai, Nuo Chen, Yiwei Gong, Bingsheng He*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2512.02589) · `system`

4. **AI-Press: A Multi-Agent News Generating and Feedback Simulation System**

    *Zhao, Xiawei, Zhou, Zhiming, Song, Kaidi, Li, Qi*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2410.07561) · `system`

5. **MARG: Multi-Agent Review Generation for Scientific Papers**

    *Mike D'Arcy, Tom Hope, Larry Birnbaum, Doug Downey*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2401.04259) · `system`

6. **ResearchAgent: Iterative Research Idea Generation over Scientific Literature**

    *Baek, Jinheon, Jauhar, Sujay Kumar, Tran, Silviu, Yoon, Sung Min*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2404.07738) · `system`

7. **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery**

    *Lu, Chris, Lu, Cong, Lange, Robert Tjarko, Foerster, Jakob, Clune, Jeff, Ha, David*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2408.06292) · `system`

8. **STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking**

    *Shao, Yijia, Jiang, Yucheng, Kanell, Theodore A., Xu, Peter, Khattab, Omar, Lam, Monica S.*

    NAACL, 2024. [`published`](https://arxiv.org/abs/2402.14207) · `system`


## [2D Visual Artifacts](#content)

### [Data Visualization](#content)

1. **MultiVis-Agent: A Multi-Agent Framework with Logic Rules for Reliable Cross-Modal Data Visualization**

    *Jinwei Lu, Yuanfeng Song, Chen Zhang, Raymond Chi-Wing Wong*

    SIGMOD, 2026. [`published`](https://arxiv.org/abs/2601.18320) · `system`

2. **PlotGen: Multi-Agent LLM-based Scientific Data Visualization**

    *Kanika Goswami, Puneet Mathur, Ryan Rossi, Franck Dernoncourt*

    ACM IUI 2025, 2025. [`published`](https://arxiv.org/abs/2502.00988) · `system`

3. **A2P-Vis: an Analyzer-to-Presenter Agentic Pipeline for Visual Insights Generation and Reporting**

    *Shuyu Gan, Renxiang Wang, James Mooney, Dongyeop Kang*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2512.22101) · `system`

4. **CoDA: Agentic Systems for Collaborative Data Visualization**

    *Zichen Chen, Jiefeng Chen, Sercan Ö. Arık, Misha Sra, Tomas Pfister, Jinsung Yoon*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.03194) · `system`

5. **DataWink: Reusing and Adapting SVG-based Visualization Examples with Large Multimodal Models**

    *Liwenhan Xie, Yanna Lin, Can Liu, Huamin Qu, Xinhuan Shu*

    VIS, 2025. [`published`](https://arxiv.org/abs/2507.17734) · `system`

6. **MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization**

    *Zhiyu Yang, Zihan Zhou, Shuo Wang, Xin Cong, Xu Han, Yukun Yan, Zhenghao Liu, Zhixing Tan, Pengyuan Liu, Dong Yu, Zhiyuan Liu, Xiaodong Shi, Maosong Sun*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2402.11453) · `system`

### [Figures, Diagrams, and Schematics](#content)

1. **AutoFigure-Edit: Generating Editable Scientific Illustration**

    *Zhen Lin, Qiujie Xie, Minjun Zhu, Shichen Li, Qiyao Sun, Enhao Gu, Yiran Ding, Ke Sun, Fang Guo, Panzhong Lu, Zhiyuan Ning, Yixuan Weng, Yue Zhang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2603.06674) · `system`

2. **EvoDiagram: Agentic Editable Diagram Creation via Design Expertise Evolution**

    *Tianfu Wang, Leilei Ding, Ziyang Tao, Yi Zhan, Zhiyuan Ma, Wei Wu, Yuxuan Lei, Yuan Feng, Junyang Wang, Yin Wu, Yizhao Xu, Hongyuan Zhu, Qi Liu, Nicholas Jing Yuan, Yanyong Zhang, Hui Xiong*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.09568) · `system`

3. **GenAI-DrawIO-Creator: A Framework for Automated Diagram Generation**

    *Jinze Yu, Dayuan Jiang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.05162) · `system`

4. **PaperBanana: Automating Academic Illustration for AI Scientists**

    *Dawei Zhu, Rui Meng, Yale Song, Xiyu Wei, Sujian Li, Tomas Pfister, Jinsung Yoon*

    arXiv, 2026. [`preprint`](https://icml.cc/virtual/2026/poster/65206) · `system`

5. **PCBSchemaGen: Constraint-Guided Schematic Design via LLM for Printed Circuit Boards**

    *Huanghaohe Zou, Peng Han, Emad Nazerian, Alex Q. Huang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.00510) · `system`

6. **SAGE: Structured Agentic Graph Editing for Software Diagrams**

    *Tyler Sivertsen, Neal Singh, James C. Davis*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2607.01102) · `system`

7. **SciFig: Towards Automating Scientific Figure Generation**

    *Siyuan Huang, Yutong Gao, Juyang Bai, Yifan Zhou, Zi Yin, Xinxin Liu, Rama Chellappa, Chun Pong Lau, Sayan Nag, Cheng Peng, Shraman Pramanick*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.04390) · `system`

8. **SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing**

    *Tong Zhang, Honglin Lin, Zhou Liu, Chong Chen, Wentao Zhang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.09809) · `benchmark`

9. **AutoFigure: Generating and Refining Publication-Ready Scientific Illustrations**

    *Minjun Zhu, Zhen Lin, Yixuan Weng, Panzhong Lu, et al.*

    ICLR, 2026. [`published`](https://arxiv.org/abs/2602.03828) · `system`

10. **From Pixels to Paths: A Multi-Agent Framework for Editable Scientific Illustration**

    *Jianwen Sun, Fanrui Zhang, Yukang Feng, Chuanhao Li, Zizhen Li, Jiaxin Ai, Yifan Chang, Yu Dai, Kaipeng Zhang*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.27452) · `system`

11. **From Words to Structured Visuals: A Benchmark and Framework for Text-to-Diagram Generation and Editing**

    *Jingxuan Wei, Cheng Tan, Qi Chen, Gaowei Wu, et al.*

    CVPR, 2025. [`published`](https://arxiv.org/abs/2411.11916) · `benchmark`

12. **LLM Code Customization with Visual Results: A Benchmark on TikZ**

    *Charly Reux, Mathieu Acher, Djamel Eddine Khelladi, Olivier Barais, Clément Quinton*

    EASE, 2025. [`published`](https://arxiv.org/abs/2505.04670) · `benchmark`

13. **SciSketch: An Open-source Framework for Automated Schematic Diagram Generation in Scientific Papers**

    *Zihang Wang, Yilun Zhao, Kaiyan Zhang, Chen Zhao, Manasi Patwardhan, Arman Cohan*

    EMNLP Demos, 2025. [`published`](https://aclanthology.org/2025.emnlp-demos.28.pdf) · `system`

14. **SketchAgent: Generating Structured Diagrams from Hand-Drawn Sketches**

    *Cheng Tan, Qi Chen, Jingxuan Wei, et al.*

    IJCAI, 2025. [`published`](https://arxiv.org/abs/2508.01237) · `system`

### [Images and Graphic Design](#content)

1. **Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling**

    *Ruijie Ye, Jiayi Zhang, Zhuoxin Liu, Zihao Zhu, Siyuan Yang, Li Li, Tianfu Fu, Franck Dernoncourt, Yue Zhao, Jiacheng Zhu, Ryan Rossi, Wenhao Chai, Zhengzhong Tu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.09084) · `system`

2. **Agentic Retoucher for Text-To-Image Generation**

    *Shaocheng Shen, Jianfeng Liang, Chunlei Cai, Cong Geng, Huiyu Duan, Xiaoyun Zhang, Qiang Hu, Guangtao Zhai*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.02046) · `system`

3. **CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator**

    *Yuhan Pu, Hao Zheng, Ziqian Mo, Hill Zhang et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.03156) · `system`

4. **CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration**

    *Hairui Zhu, Yiying Yang, Tengjin Weng, Ziyu Lu, Xiao Yao, Xiaoyang Ye, Lin Ma, Wenhao Jiang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2607.05465) · `system`

5. **GraphicBench: A Planning Benchmark for Graphic Design with Language Agents**

    *Dayeon Ki, Tianyi Zhou, Marine Carpuat, Gang Wu, Puneet Mathur, Viswanathan Swaminathan*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2504.11571) · `benchmark`

6. **Mirror in the Model: Ad Banner Image Generation via Reflective Multi-Agent**

    *Zhao Wang, Bowen Chen, Yotaro Shimose, Sota Moriyama, Heng Wang, Shingo Takamatsu*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2507.03326) · `system`

7. **SketchAgent: Language-Driven Sequential Sketch Generation**

    *Yael Vinker, Tamar Rott Shaham, Kristine Zheng, Alex Zhao, Judith E. Fan, Antonio Torralba*

    CVPR, 2025. [`published`](https://arxiv.org/abs/2411.17673) · `system`

8. **BannerAgency: Advertising Banner Design with Multimodal LLM Agents**

    *Heng Wang, Yotaro Shimose, Shingo Takamatsu*

    EMNLP, 2025. [`published`](https://arxiv.org/abs/2503.11060) · `system`

9. **T2I-Copilot: A Training-Free Multi-Agent Text-to-Image System for Enhanced Prompt Interpretation and Interactive Generation**

    *Chieh-Yun Chen, Min Shi, Gong Zhang, Humphrey Shi*

    ICCV, 2025. [`published`](https://arxiv.org/abs/2507.20536) · `system`

### [Posters](#content)

1. **AutoPP: Towards Automated Product Poster Generation and Optimization**

    *Jiahao Fan, Yuxin Qin, Wei Feng, Yanyin Chen, et al.*

    AAAI, 2026. [`published`](https://arxiv.org/abs/2512.21921) · `system`

2. **PosterForest: Hierarchical Multi-Agent Collaboration for Scientific Poster Generation**

    *Jiho Choi, Seojeong Park, Seongjong Song, Hyunjung Shim*

    arXiv, 2026. [`preprint`](https://aclanthology.org/2026.acl-long.15/) · `system`

3. **P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark**

    *Tao Sun, Enhao Pan, Zhengkai Yang, Kaixin Sui, Jiajun Shi, Xianfu Cheng, Tongliang Li, Wenhao Huang, Ge Zhang, Jian Yang, Zhoujun Li*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2505.17104) · `benchmark`

4. **Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers**

    *Wei Pang, Kevin Qinghong Lin, Xiangru Jian, Xi He, Philip Torr*

    NeurIPS, 2025. [`published`](https://arxiv.org/abs/2505.21497) · `system`

### [Presentations](#content)

1. **DECKBench: Benchmarking Multi-Agent Frameworks for Academic Slide Generation and Editing**

    *Daesik Jang, Morgan Lindsay Heisler, Linzi Xing, Yifei Li, Edward Wang, Ying Xiong, Yong Zhang, Zhenan Fan*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.13318) · `benchmark`

2. **DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation**

    *Hao Zheng, Guozhao Mo, Xinru Yan, et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.22839) · `system`

3. **Narrative-Driven Paper-to-Slide Generation via ArcDeck**

    *Tarik Can Ozden, Sachidanand VS, Furkan Horoz, Ozgur Kara, Junho Kim, James Matthew Rehg*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.11969) · `system`

4. **SlidesGen-Bench: Evaluating Slides Generation via Computational and Quantitative Metrics**

    *Yunqiao Yang, Wenbo Li, Houxing Ren, Zimu Lu, Ke Wang, Zhiyuan Huang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.09487) · `benchmark`

5. **SlideBot: A Multi-Agent Framework for Generating Informative, Reliable, Multi-Modal Presentations**

    *Eric Xie, Danielle Waterfield, Michael Kennedy, Aidong Zhang*

    EAAI, 2026. [`published`](https://arxiv.org/abs/2511.09804) · `system`

6. **Auto-Slides: An Interactive Multi-Agent System for Creating and Customizing Presentation Slides**

    *Yuheng Yang, Wenjia Jiang, Yang Wang, Yi Song, Yiwei Wang, Chi Zhang*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.11062) · `system`

7. **PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides**

    *Hao Zheng, Xinyan Guan, Hao Liu, Yankai Lin, Jizhong Han, Jie Chen*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2501.03936) · `benchmark`

8. **SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation**

    *Xin Liang, Xiang Zhang, Yiwei Xu, Siqi Sun, Chenyu You*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2512.04529) · `system`

9. **PreGenie: An Agentic Framework for High-quality Visual Presentation Generation**

    *Xiaojie Xu, Xinli Xu, Sirui Chen, Haoyu Chen, Fan Zhang, Ying-Cong Chen*

    EMNLP Findings, 2025. [`published`](https://arxiv.org/abs/2505.21660) · `system`


## [Music and Audio Artifacts](#content)

### [Music Composition](#content)

1. **Libretto: Giving LLM Agents a Sense of Musical Structure**

    *Yichen Xu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2606.22708) · `system`

2. **CoComposer: LLM Multi-agent Collaborative Music Composition**

    *Peiwen Xing, Aske Plaat, Niki van Stein*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.00132) · `system`

3. **MusicSwarm: Biologically Inspired Intelligence for Music Composition**

    *Markus J. Buehler*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.11973) · `system`

4. **WeaveMuse: An Open Agentic System for Multimodal Music Understanding and Generation**

    *Emmanouil Karystinaios*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.11183) · `system`

5. **ComposerX: Multi-Agent Symbolic Music Composition with LLMs**

    *Qixin Deng, Qikai Yang, Ruibin Yuan, et al.*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2404.18081) · `system`

### [Produced and Spoken Audio](#content)

1. **Feedback-Driven Retrieval-Augmented Audio Generation with Large Audio Language Models**

    *Junqi Zhao, Chenxing Li, Jinzheng Zhao, Rilin Chen, Dong Yu, Mark D. Plumbley, Wenwu Wang*

    ICASSP, 2026. [`published`](https://doi.org/10.1109/ICASSP55912.2026.11462219) · `system`

2. **AI4Reading: Chinese Audiobook Interpretation System Based on Multi-Agent Collaboration**

    *Minjiang Huang, Jipeng Qiang, Yi Zhu, Chaowei Zhang, Xiangyu Zhao, Kui Yu*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2512.23300) · `system`

3. **Orchestrating Audio: Multi-Agent Framework for Long-Video Audio Synthesis**

    *Yehang Zhang, Xinli Xu, Xiaojie Xu, Doudou Zhang, Li Liu, Ying-Cong Chen*

    EMNLP, 2025. [`published`](https://aclanthology.org/2025.emnlp-main.1133/) · `system`, [`code`](https://lvas-agent.github.io)

4. **WavCraft: Audio Editing and Generation with Large Language Models**

    *Jinhua Liang, Huan Zhang, Haohe Liu, Yin Cao, Qiuqiang Kong, Xubo Liu, Wenwu Wang, Mark D. Plumbley, Huy Phan, Emmanouil Benetos*

    ICLR Workshop, 2024. [`published`](https://openreview.net/forum?id=xJw7x2ZBex) · `system`, [`code`](https://github.com/JinhuaLiang/WavCraft)


## [Video and Animation Artifacts](#content)

### [Explainer and Presentation Video](#content)

1. **Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Editing**

    *Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.11790) · `system`

2. **ManimAgent: Self-Evolving Multimodal Agents for Visual Education**

    *Wenjia Jiang, Zongyuan Cai, Yuanhang Shao, Chenru Wang, Boyan Han, Zhixue Song, Keyu Chen, Shengwei An, Xu Yang, Zhou Yang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2606.30296) · `system`

3. **Code2Video: A Code-centric Paradigm for Educational Video Generation**

    *Yanzhe Chen, Kevin Qinghong Lin, Mike Zheng Shou*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.01174) · `system`

4. **Paper2Video: Automatic Video Generation from Scientific Papers**

    *Zeyu Zhu, Kevin Qinghong Lin, Mike Zheng Shou*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.05096) · `system`

### [Narrative and Cinematic Video](#content)

1. **Agentic Video Generation: From Text to Executable Event Graphs via Tool-Constrained LLM Planning**

    *Nicolae Cudlenco, Mihai Masala, Marius Leordeanu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.10383) · `system`

2. **MUSE: A Multi-agent Framework for Unconstrained Story Envisioning via Closed-Loop Cognitive Orchestration**

    *Wenzhang Sun, Zhenyu Wang, Zhangchi Hu, Chunfeng Wang, Hao Li, Wei Chen*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.03028) · `system`

3. **SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scene Text-to-Video**

    *Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.05489) · `system`

4. **HAMLET: A Hierarchical and Adaptive Multi-Agent Framework for Live Embodied Theatrics**

    *Shufan Jiang, Sizhou Chen, Chi Zhang, Xiao-Lei Zhang, Xuelong Li*

    ICLR, 2026. [`published`](https://arxiv.org/abs/2507.15518) · `system`

5. **Hollywood Town: Long-Video Generation via Cross-Modal Multi-Agent Orchestration**

    *Zheng Wei, Mingchen Li, Zeqian Zhang, Ruibin Yuan, Pan Hui, Huamin Qu, James Evans, Maneesh Agrawala, Anyi Rao*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.22431) · `system`

6. **GenMAC: Compositional Text-to-Video Generation with Multi-Agent Collaboration**

    *Kaiyi Huang, Yukun Huang, Xuefei Ning, Zinan Lin, Yu Wang, Xihui Liu*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2412.04440) · `system`

### [Personalized and Branded Video](#content)

1. **BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation**

    *Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2603.02816) · `system`

2. **AutoMV: An Automatic Multi-Agent System for Music Video Generation**

    *Xiaoxuan Tang, Xinping Lei, Chaoran Zhu, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2512.12196) · `system`

3. **PersonaVlog: Personalized Multimodal Vlog Generation with Multi-Agent Collaboration and Iterative Self-Correction**

    *Xiaolu Hou, Bing Ma, Jiaxiang Cheng, Xuhua Ren, Kai Yu, Wenyue Li, Tianxiang Zheng, Qinglin Lu*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2508.13602) · `system`

### [Video Editing and Refinement](#content)

1. **GLANCE: A Global-Local Coordination Multi-Agent Framework for Music-Grounded Mashup Video Creation**

    *Zihao Lin, Haibo Wang, Zhiyang Xu, Siyao Dai et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.05076) · `system`

2. **StoryBlender: Inter-Shot Consistent and Editable 3D Storyboard with Spatial Intelligence**

    *Bingliang Li, Zhenhong Sun, Jiaming Bian, Yuehao Wu et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.03315) · `system`

3. **VideoMemory: Toward Consistent Video Generation via Memory Integration**

    *Jinsong Zhou, Yihua Du, Xinli Xu, Luozhou Wang et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.03655) · `system`

4. **FantasyHSI: Video-Generation-Centric 4D Human Synthesis In Any Scene through A Graph-based Multi-Agent Framework**

    *Lingzhou Mu, Qiang Wang, Fan Jiang, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.01232) · `system`

5. **From Shots to Stories: LLM-Assisted Video Editing with Unified Language Representations**

    *Yuzhi Li, Haojun Xu, Feng Tian*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2505.12237) · `system`

6. **UniVA: Universal Video Agent towards Open-Source Next-Generation Video Generalist**

    *Zhengyang Liang, Daoan Zhang, Huichi Zhou, Rui Huang, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2511.08521) · `system`

7. **VISTA: A Test-Time Self-Improving Video Generation Agent**

    *Do Xuan Long, Xingchen Wan, Hootan Nakhost, Chen-Yu Lee et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.15831) · `system`

8. **EditDuet: A Multi-Agent System for Video Non-Linear Editing**

    *Marcelo Sandoval-Castaneda, Bryan Russell, Josef Sivic, Gregory Shakhnarovich, Fabian Caba Heilbron*

    SIGGRAPH, 2025. [`published`](https://arxiv.org/abs/2509.10761) · `system`

### [Animation](#content)

1. **AnimAgents: Coordinating Multi-Stage Animation Pre-Production with Human-Multi-Agent Collaboration**

    *Wen-Fan Wang, Chien-Ting Lu, Jin Ping Ng, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2511.17906) · `system`

2. **AniMaker: Multi-Agent Animated Storytelling with MCTS-Driven Clip Generation**

    *Haoyuan Shi, Yunxin Li, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2506.10540) · `system`

3. **AniME: Adaptive Multi-Agent Planning for Long Animation Generation**

    *Lisai Zhang, Baohan Xu, Siqian Yang, Mingyu Yin, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2508.18781) · `system`

4. **MapStory: Prototyping Editable Map Animations with LLM Agents**

    *Aditya Gunturu, Ben Pearman, Keiichi Ihara, Morteza Faraji, Bryan Wang, Rubaiat Habib Kazi, Ryo Suzuki*

    UIST, 2025. [`published`](https://arxiv.org/abs/2505.21966) · `system`

5. **CoMA: Compositional Human Motion Generation with Multi-modal Agents**

    *Shanlin Sun, Gabriel De Araujo, Jiaqi Xu, et al.*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2412.07320) · `system`


## [3D and Spatial Artifacts](#content)

### [3D Objects and Assets](#content)

1. **EZBlender: Efficient 3D Editing with Plan-and-ReAct Agent**

    *Hao Wang, Wenhui Zhu, Shao Tang, Zhipeng Wang, Xuanzhao Dong, Xin Li, Xiwen Chen, Ashish Bastola, Xinhao Huang, Yalin Wang, Abolfazl Razi*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.07143) · `system`

2. **LL3M: Large Language 3D Modelers**

    *Sining Lu, Guan Chen, Nam Anh Dinh, Itai Lang, Ari Holtzman, Rana Hanocka*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2508.08228) · `system`

3. **SmartAvatar: Text- and Image-Guided Human Avatar Generation with VLM AI Agents**

    *Alexander Huang-Menders, Xinhang Liu, Andy Xu, Yuyao Zhang, Chi-Keung Tang, Yu-Wing Tai*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2506.04606) · `system`

4. **ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling**

    *Shuyuan Zhang, Chenhan Jiang, Zuoou Li, Jiankang Deng*

    NeurIPS, 2025. [`published`](https://arxiv.org/abs/2510.17603) · `system`

### [3D Scenes and Worlds](#content)

1. **Code2Worlds: Empowering Coding LLMs for 4D World Generation**

    *Yi Zhang, Yunshuang Wang, Zeyu Zhang, Hao Tang*

    arXiv, 2026. [`preprint`](https://icml.cc/virtual/2026/poster/64546) · `system`

2. **MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction**

    *Ruijie Xu, Xinnan Zhu, Jiayu Ying, Daoguo Dong, Yuzhou Ji, Xin Tan*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2606.14168) · `system`

3. **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI**

    *Hongchi Xia, Xuan Li, Zhaoshuo Li, Qianli Ma, et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.10116) · `system`

4. **SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes**

    *Nicholas Pfaff, Thomas Cohn, Sergey Zakharov, Rick Cory, Russ Tedrake*

    arXiv, 2026. [`preprint`](https://icml.cc/virtual/2026/poster/63465) · `system`

5. **Agentic 3D Scene Generation with Spatially Contextualized VLMs**

    *Xinhang Liu, Yu-Wing Tai, Chi-Keung Tang*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2505.20129) · `system`

6. **RAISECity: A Multimodal Agent Framework for Reality-Aligned 3D World Generation at City-Scale**

    *Shengyuan Wang, Zhiheng Zheng, Yu Shang, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2511.18005) · `system`

7. **RoomPlanner: Explicit Layout Planner for Easier LLM-Driven 3D Room Generation**

    *Wenzhuo Sun, Mingjian Liang, Wenxuan Song, Xuelian Cheng, Zongyuan Ge*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2511.17048) · `system`

8. **WorldCraft: Photo-Realistic 3D World Creation and Customization via LLM Agents**

    *Xinhang Liu, Chi-Keung Tang, Yu-Wing Tai*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2502.15601) · `system`

9. **Scenethesis: A Language and Vision Agentic Framework for 3D Scene Synthesis**

    *Lu Ling, Chen-Hsuan Lin, Tsung-Yi Lin, Yifan Ding, Yu Zeng, Yichen Sheng, Yunhao Ge, Ming-Yu Liu, Aniket Bera, Zhaoshuo Li*

    ICLR 2026, 2025. [`published`](https://arxiv.org/abs/2505.02836) · `system`

### [CAD and Engineering Geometry](#content)

1. **ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation**

    *Yunhan Xu, Qifeng Wu, Xunjin Li, Yuanwei Bin, Qingsong Yao, Jianghang Gu, Guan Wang, Weihao Lv, Huiyu Yang, Wenfa Luo, Jiao Xiang, Yuntian Chen, Shiyi Chen*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2607.05750) · `system`

2. **TurboAgent: An LLM-Driven Autonomous Multi-Agent Framework for Turbomachinery Aerodynamic Design**

    *Juan Du, Yueteng Wu, Pan Zhao, Yuze Liu, Min Zhang, Xiaobin Xu, Xinglong Zhang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.06747) · `system`

3. **3Dify: a Framework for Procedural 3D-CG Generation Assisted by LLMs Using MCP and RAG**

    *Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Satoshi Ohshima, Takahiro Katagiri*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.04536) · `system`

4. **CADDesigner: Conceptual Design of CAD Models Based on General-Purpose Agent**

    *Fengxiao Fan, Jingzhe Ni, Xiaolong Yin, Sirui Wang, Xingyu Lu, Qiang Zou, Ruofeng Tong, Min Tang, Peng Du*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2508.01031) · `system`

5. **Generative AI for CAD Automation: Leveraging Large Language Models for 3D Modelling**

    *Sumit Kumar, Sarthak Kapoor, Harsh Vardhan, Yao Zhao*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2508.00843) · `system`

6. **Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference**

    *Xueyang Li, Jiahao Li, Yu Song, Yunzhong Lou, Xiangdong Zhou*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2505.17702) · `system`

7. **Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM**

    *Abir Khan Ratul, Sanjay Acharjee, Somin Park, Md Nazmus Sakib*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.20838) · `system`

8. **MEDA: A Multi-Agent System For Parametric CAD Model Creation**

    *Nirmal Panta, Sakar Kafley, Rabi Acharya, Samridh Parajuli, Dipesh Parajuli, Pradip Panta, Sujan Belbase, Saurab Pant, Amit Regmi, Atsushi Tanaka, Christopher McComb*

    ASME IDETC-CIE 2025, 2025. [`published`](https://jglobal.jst.go.jp/en/public/202602245987265300) · `system`


## [Software and Executable Artifacts](#content)

### [Applications and Code Repositories](#content)

1. **ComfySearch: Autonomous Exploration and Reasoning for ComfyUI Workflows**

    *Jinwei Su, Qizhen Lan, Zeyu Wang, et al.*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2601.04060) · `system`

2. **Compiling Large Multi-Modal Requirement Documents into Runnable Software Systems: From an Agentic Test-Driven Perspective**

    *Weiyu Kong, Yun Lin, Xiwen Teoh, Duc-Minh Nguyen, Ruofei Ren, Jiaxin Chang, Haoxu Hu, Haoyu Chen*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.13723) · `system`

3. **CodeCRDT: Observation-Driven Coordination for Multi-Agent LLM Code Generation**

    *Sergey Pugachev*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.18893) · `system`

4. **Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI Agents**

    *Jiacheng Miao, Joe R. Davis, Yaohui Zhang, Jonathan K. Pritchard, James Zou*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.06917) · `system`

5. **CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-Level Coding Challenges**

    *Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, Zhi Jin*

    ACL, 2024. [`published`](https://arxiv.org/abs/2401.07339) · `system`

6. **AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation**

    *Dong Huang, Jie M. Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, Heming Cui*

    arXiv, 2024. [`preprint`](https://arxiv.org/abs/2312.13010) · `system`

### [Websites and User Interfaces](#content)

1. **Human-Agent Collaborative Paper-to-Page Crafting**

    *Qianli Ma, Siyu Wang, Yilin Chen, Yinhao Tang, Yixiang Yang, Chang Guo, Bingjie Gao, Zhening Xing, Yanan Sun, Zhipeng Zhang*

    arXiv, 2026. [`preprint`](https://aclanthology.org/2026.findings-acl.1988/) · `system`

2. **Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification**

    *Zehai He, Wenyi Hong, Zhen Yang, Ziyang Pan, Mingdao Liu, Xiaotao Gu, Jie Tang*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2603.26648) · `benchmark`

3. **VisionRefine: Vision-Guided Iterative Refinement for Frontend Code Generation**

    *Hannah Sansford, Derek H. C. Law, Wei Liu, Abhishek Tripathi, Niresh Agarwal, Gerrit J. J. van den Burg*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.05839) · `system`

4. **ViviDoc: Generating Interactive Documents through Human-Agent Collaboration**

    *Yinghao Tang, Yupeng Xie, Yingchaojie Feng, Tingfeng Lan, Wei Chen*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2603.01912) · `system`

5. **DuetUI: A Bidirectional Context Loop for Human-Agent Co-Generation of Task-Oriented Interfaces**

    *Yuan Xu, Shaowen Xiang, Yizhi Song, Ruoting Sun, Xin Tong*

    CHI, 2026. [`published`](https://arxiv.org/abs/2509.13444) · `system`

6. **Computer-Use Agents as Judges for Generative User Interface**

    *Kevin Qinghong Lin, Siyuan Hu, Linjie Li, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2511.15567) · `system`

7. **DashChat: Interactive Authoring of Industrial Dashboard Design Prototypes through Conversation with LLM-Powered Agents**

    *S. Shen, Z. Lin, W. Liu, C. Xin, W. Dai, S. Chen, X. Wen, X. Lan*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2504.12865) · `system`

8. **Paper2Web: Let's Make Your Paper Alive!**

    *Yuhang Chen, Tianpeng Lv, Siyi Zhang, Yixiang Yin, Yao Wan, Philip S. Yu, Dongping Chen*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2510.15842) · `system`

9. **WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning**

    *Zimu Lu, Houxing Ren, Yunqiao Yang, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.22644) · `system`

10. **WebVIA: A Web-based Vision-Language Agentic Framework for Interactive and Verifiable UI-to-Code Generation**

    *Mingde Xu, Zhen Yang, Wenyi Hong, et al.*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2511.06251) · `system`

### [Games and Simulations](#content)

1. **AutoUE: Automated Generation of 3D Games in Unreal Engine via Multi-Agent Collaboration**

    *Lei Yin, Wentao Cheng, Zhida Qin, Tianyu Huang, Yidong Li, Gangyi Ding*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2603.07106) · `system`

2. **OpenGame: Open Agentic Coding for Games**

    *Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, Jiaming Han, Tianshuo Peng, Kaixuan Fan, Manyuan Zhang, Xiangyu Yue*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2604.18394) · `system`

3. **ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas**

    *Wenjun Peng, Xinyu Wang, Qi Wu*

    arXiv, 2026. [`preprint`](https://arxiv.org/abs/2602.04296) · `benchmark`

4. **90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development**

    *Runxin Yang, Yuxuan Wan, Shuqing Li, Michael R. Lyu*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.26161) · `system`

5. **Multi-Agent Game Generation and Evaluation via Audio-Visual Recordings**

    *Alexia Jolicoeur-Martineau*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2508.00632) · `system`

6. **Story2Game: Generating Interactive Fiction Games from Stories**

    *Eric Zhou, Shreyas Basavatia, Moontashir Siam, Zexin Chen, Mark O. Riedl*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2505.03547) · `system`

7. **V-GameGym: Visual Game Generation for Code Large Language Models**

    *Wei Zhang, Jack Yang, Renshuai Tao, Lingzheng Chai, Shawn Guo, Jiajun Wu, Xiaoming Chen, Ganqu Cui, Ning Ding, Xander Xu, Hu Wei, Bowen Zhou*

    arXiv, 2025. [`preprint`](https://arxiv.org/abs/2509.20136) · `benchmark`

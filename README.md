# 🐋 WADER 
Implementation of the paper [A Weak-labelling framework for Data augmentation in tExt Regression Tasks](https://arxiv.org/abs/2303.02758) under review at SemEval 2023, colocated with ACL 2023.

![WADER DIAGRAM](https://cdn.discordapp.com/attachments/891317274936483871/1088939844782264330/WADER_diagrams-Copy_of_Page-1.drawio.png)

Intimacy is an essential element of human relationships and language is a crucial means of conveying it. Textual intimacy analysis can reveal social norms in different contexts and serve as a benchmark for testing computational models’ ability to understand social information. In this paper, we propose a novel weak-labeling strategy for data augmentation in text regression tasks called WADER. WADER uses data augmentation to address the problems of data imbalance and data scarcity and provides a method for data augmentation in cross-lingual, zero-shot tasks. We benchmark the performance of State-of-the-Art pretrained multilingual language models using WADER and analyze the use of sampling techniques to mitigate bias in data and optimally select augmentation candidates. Our results show that WADER outperforms the baseline model and provides a direction for mitigating data imbalance and scarcity in text regression tasks. 
## 🤝 Main Contributions 
1. Provide a data augmentation framework specific to text regression.
2. Provide a method for data augmentation in cross-lingual, zero-shot tasks.
3. Benchmark performance of pre-trained language models.
4. Analysis of use of sampling techniques to mitigate bias in data and optimally select augmentation candidates.
## 📝 Task Description
SemEval 2023 Task 9: Multilingual Tweet Intimacy Analysis (Pei et al., 2022) is a task that deals with detecting intimacy in 10 languages. This task is co-organized by University of Michigan and Snap Inc. Intimacy is a fundamental aspect of human relationships, and studying intimacy in a textual context has many potential applications in the field of computational linguistics. The training data is available in 6 languages: English, Spanish, Italian, Portuguese, French, and Chinese. The evaluation is done on the given training languages, as well as 6 unseen languages: Hindi, Arabic, Dutch and Korean.
## 🔨 Dependencies
1. `simpletransformers`
2. `pandas`
3. `numpy`
4. `sklearn`
5. `googletrans`
6. `matplotlib`
## 🖊 Citation
```
@misc{suri2023wader,
      title={WADER at SemEval-2023 Task 9: A Weak-labelling framework for Data augmentation in tExt Regression Tasks}, 
      author={Manan Suri and Aaryak Garg and Divya Chaudhary and Ian Gorton and Bijendra Kumar},
      year={2023},
      eprint={2303.02758},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

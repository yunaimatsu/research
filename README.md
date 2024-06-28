[日本語](#)
[English]

> 日本語
# 
# 研究に関する情報を全て公開するレポジトリ
このREADMEでは、わたくし松浦の研究について詳細にまとめております。以下のような構成です。
1. 研究の大きな「最終目標」を掲げる。
2. そのために必要な基礎研究を検討する。
3. 基礎研究の1つとして私の卒業研究を位置付けて説明する。

# 最終目標：全世界の言語をAI翻訳に対応させる
1. 世界中の「言語」を記述する。
2. 世界中の「言語」をリストアップし、ネイティブによる容認性判断を行う。
3. ネイティブによる容認性が低い言語(less-documented languageと呼ぶ)を割り出し、それらと系統が近い言語を用意する。
4. 系統が近い言語たちで事前学習済みモデルを作成する。
5. そのless-documented languageで集めたテキストでファインチューニングを行う。
6. ファインチューニングを行ったモデルで、もう一度容認性判断を行う。

# 1. False-friendsの意味の差を数値化する
## 1.1. False-friendsとは何か？
**語源は同じだが、意味が異なる単語のペア**のことです。
例えば、英語**to ignore**とフランス語**ignorer**はどちらも、ラテン語の**ignōrāre**から派生しています。しかし英語の場合は「**無視する**」という意味なのに対し フランス語では「**を知らない**」という意味になります。
このto ignoreとignorerのような、「語源は一緒だけど意味が違う」組み合わせのことを、**False-friends**と呼びます。
## 1.2. なぜFalse-friendsの意味の差を数値化するのか？
最終的に言語間の距離を算出するためです。
これまでの[言語統計学](https://en.wikipedia.org/wiki/Linguistic_distance)では、「語源が同じ単語を共有する割合」によって言語間の距離が算出されて来ました。
しかし、その手法は比較的 **"違う"** 言語でしか有用ではありません。
「方言」と言えるほど近い言語たちは同語源の単語を多く共有します。そのため、そのような割合の差を算出しても誤差程度にしかならず、新たなインサイトをやることはできません。
## 1.3. どのように数値化するのか？
以下の2ステップで行います。
1. 個々の単語の**意味をベクトル(実数の集合)に変換**する
2. 単語同士のベクトルの**コサイン類似度を算出**する
### 1.3.1. 意味をベクトルに変換する
この作業のアルゴリズムはここで説明するにはあまりにも複雑であるため割愛します。ただ、誤解されそうな点を中心に完結に説明します。
#### 文脈に基づいてベクトル化されています
ベクトル化の作業は、決してでたらめに行なっているわけではありません。一緒に出てくる単語などを元に統計的に調整された数値です。
#### 元となる文章の種類やサイズによって異なります
前項を踏まえると、想像に難くないと思います。大量の文章データであるほどより多くの単語データが確保でき、質・量共に性能が向上します。
### 1.3.2. コサイン類似度を算出する
ベクトルは実数の集合であるため、通常の四則演算ではなく、コサイン類似度を用いて差を算出します。

> English

## Research Information Repository

This README provides a detailed summary of my research, Matsuura's research. It is organized as follows:
1. State the major "ultimate goal" of the research.
2. Consider the fundamental research necessary to achieve this goal.
3. Position and explain my graduation research as one of the foundational studies.

## Ultimate Goal: Enable AI Translation for All Languages Worldwide

1. Describe the "languages" of the world.
2. List the "languages" of the world and conduct acceptability judgments by native speakers.
3. Identify languages with low native speaker acceptability (referred to as less-documented languages) and prepare closely related languages.
4. Create pre-trained models with the closely related languages.
5. Fine-tune these models using texts collected in the less-documented languages.
6. Conduct acceptability judgments again using the fine-tuned models.

## 1. Quantifying the Meaning Differences of False Friends

### 1.1. What are False Friends?

False friends are pairs of words that have the same etymology but different meanings. For example, the English word **to ignore** and the French word **ignorer** both derive from the Latin **ignōrāre**. However, in English, it means "**to disregard**," whereas in French it means "**to not know**." Such pairs, where the etymology is the same but the meanings differ, are called **false friends**.

### 1.2. Why Quantify the Meaning Differences of False Friends?

The ultimate goal is to calculate the distance between languages. In traditional [linguistic distance](https://en.wikipedia.org/wiki/Linguistic_distance) studies, the distance between languages has been calculated based on the "proportion of shared etymological words." However, this method is only useful for relatively **different** languages. Languages that are as close as dialects share many etymological words. Therefore, calculating the differences in such proportions would result in negligible errors and would not provide new insights.

### 1.3. How to Quantify the Differences?

This is done in two steps:
1. **Convert the meanings of individual words into vectors (sets of real numbers).**
2. **Calculate the cosine similarity between word vectors.**

#### 1.3.1. Converting Meanings into Vectors

The algorithm for this task is too complex to explain here, but I will provide a brief explanation focusing on points that may be misunderstood.

- **Based on context:** The vectorization process is not done randomly but is statistically adjusted based on the context in which the words appear together.
- **Varies by the type and size of the source text:** This should be easy to imagine based on the previous point. The larger the text data, the more word data can be secured, improving both the quality and quantity of performance.

#### 1.3.2. Calculating Cosine Similarity

Since vectors are sets of real numbers, we calculate the differences using cosine similarity rather than regular arithmetic operations.
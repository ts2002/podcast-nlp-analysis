
# Using Automated Transcription To Perform Topic Modeling and Sentiment Analysis on News Podcasts

## Abstract

Podcasting has become a widely popular medium of news distribution across the political belief spectrum. Despite this, textual analysis, specifically regarding topic modeling and sentiment analysis, for podcast content is relatively unexplored. In comparison to textual news media, there is an additional challenge of obtaining and pre-processing the data for analysis. This paper aims to demonstrate how these challenges can be overcome,  and understand what topics are covered within news podcasts and how sentiment may differ across sources.

To represent a variety of political beliefs and coverage scope, four podcasts associated with major news distributors were chosen: "What's News" by The Wall Street Journal, "Up First" by NPR, "FOX News Rundown" by Fox News, and "Reuters World News" by Reuters. Audio files were obtained by manual collection and by scraping RSS files, and transcribed into text using OpenAI's Whisper model.

Topic analysis was performed using the BERTopic Python module. Results demonstrated the relevance of major world events, such as the Israel-Hamas conflict, across all podcasts. Niche subjects limited to one or two podcasts were also discovered, demonstrating differences between reporting choices.

Based on the results obtained from topic modeling, sentiment analysis was done on a highly prevalent topic, Israel. This analysis revealed insights into sentiment trends over time, as well as allowing for the identification of triggers of high sentiment changes.

Overall, this research presents the study of podcast content as a promising area of textual research and provides examples for future work to draw from. However, a major problem encountered in the data was conversational or advertisement-related noise. Potential areas of future research include expanding on the provided corpus or developing strategies to mitigate podcast-specific noise.

## Introduction

Podcasting is a widely popular medium for content distribution, and news is no exception. A 2022 study [1] by the Pew Researcher Center found that 49% of American adults had listened to podcasts in the previous year, and of the podcasts they listened to, 67% of them were podcasts where news was discussed. As shown in the same study [1], this phenomenon is not a partisan trend; both parties tend to consume news information from podcasts at a similar rate. Many major news broadcasters have podcasts, such as NPR or The Wall Street Journal [2], reflecting that major industry companies see value in the medium as well.

The prevalence of textual news media in the NLP community is evident in the many news-focused datasets available such as "multi_news" [3] or studies such as Vicari and Gáspari (2020) which examine sentiment in financial publications [4]. However, in contrast to textual media, relatively little bias or sentiment analysis has been done on news podcasts. This is likely due to the higher level of effort needed to obtain and clean textual data originating from podcasts. This research aims to examine major topics discussed across a variety of news podcasts, including analyzing topic overlap and sentiment across platforms.

## Methodology/Dataset

Within this research, four podcasts were used for data: "What's News" by The Wall Street Journal [5], "Up First" by NPR [6], "FOX News Rundown" by Fox News [7], and "Reuters World News" [8]. These podcasts were chosen to represent a variety of political beliefs and the scope of news (e.g. U.S. versus World focused) from established news broadcasters. All podcasts used within this dataset were published from 3/1/2024 to 3/25/2024.

For all of these podcasts, it was not possible to directly download the audio files from their hosting websites. However, all podcasts had a corresponding RSS feed which  could be scraped to obtain the audio file download links and download the files. For all podcasts excluding "What's News", it was possible to do this with the Python script "rss_scraper.py" found in the Transcription_Tools directory without any additional steps. For "What's News", the RSS feed was limited to a smaller timeframe, requiring usage of the Wayback Machine [9] to obtain the older RSS feeds for days in March no longer included in the current feed or download audio files directly from the source. The download links in the archived RSS feed were still active and the episodes could be scraped from there if not included in the current feed.

After obtaining the audio files, the next step was to transcribe them into text files.  This was done with OpenAI's "base" Whisper model [10] which can be used to transcribe audio into text.  The code for this can be found in "mp3_to_txt_whisper.py" in the Transcription_Tools directory.  All resulting text files can be found in the Raw_Articles directory in folders corresponding to their source podcast. All podcasts do not share an identical publishing schedule so there are some differences in available dates and daily lengths (e.g. WSJ posts twice daily, so to keep the standard 1 document/day pattern, both were concatenated into one document).

The exploratory data analysis process consisted of visualizing the embedding of the top five words in each document as determined by TF_IDF, with embeddings generated with Gensim's Word2Vec function.  The code for this can be found in EDA.ipynb. Further analysis was performed by utilizing the BERTopic Python module [11] to determine primary topics of discussion in the corpus. Before topic classification I used Spacy's Sentencizer [13] to split each document into sentences to remove sentences from the document that contained regularly included advertisements (Ex: Amazon Prime). Topic modeling was also done on an individual podcast level but with analysis of sentences versus entire documents and more manual advertisement removal. Sentiment analysis was performed with the NewsSentiment target-dependent sentiment classification model [12]. This required pre-processing to split the topic into a left, middle, and right portion, where the middle portion represents the target sentiment that should be evaluated. I chose this model because it was trained on news articles, which were relevant to my data and  it allowed me to specify a target of sentiment.

## Results

### All Podcast Topic Breakdown

<figure>

<img src="https://i.imgur.com/3UZoO9Y.png" />

<div align="center">

<figcaption>Fig 1.1) Topic breakdown identified in the entire corpus (all podcasts included). </figcaption>

</div>

</figure>

Fig 1.1 shows the topic breakdown resulting from the BERTopic analysis and the top five words within each topic. Topic 0 appears to cover items related to food prices and the economy, Topic 1 covers the Israel-Hamas conflict, Topic 2 the Florida Everglades and the planned restoration project, Topic 3 the presidency and Biden, Topic 4 Ukraine, and social media, Topic 5 TikTok (and its potential ban), Topic 6 the crisis in Haiti, Topic 7 electric vehicles and Topic 8 the death of Alexei Navalny and his documentary on Netflix. The "pigs" mentioned in Topic 8 are likely related to the first human to receive a kidney from a pig, not Navalny. The model was sensitive to hyper-parameter changes and the effect of randomness when executing the fitting process. Some other topics that appeared in other versions of the model were the Oscars or the discussion of Russia or China.

<figure>

<img src="https://i.imgur.com/2FA07zj.png" />

<div align="center">

<figcaption>Fig 1.2) Topic and Document Clustering Chart </figcaption>

</div>

</figure>

Figure 1.2 shows the document clustering of different topics, where each point corresponds to a document. This provides some insight into how similar topics were evaluated to be another and the potential overlap or exclusion of documents from any topics.

### Individual Results

<figure>

<img src="https://i.imgur.com/oJhLpNQ.png" />

<div align="center">

<figcaption>Fig 1.3) WSJ Individual Topic Chart </figcaption>

</div>

</figure>

<figure>

<img src="https://i.imgur.com/ySPQIHW.png" />

<div align="center">

<figcaption>Fig 1.4) NPR Individual Chart </figcaption>

</div>

</figure>

<figure>

<img src="https://i.imgur.com/xyMbXtZ.png" />

<div align="center">

<figcaption>Fig 1.5) Reuters Individual Chart </figcaption>

</div>

</figure>

<figure>

<img src="https://i.imgur.com/kswcQzj.png"/>

<div align="center">

<figcaption>Fig 1.6) Fox Individual Chart </figcaption>

</div>

</figure>

Figures 1.3 through 1.6 illustrate the topics on an individual podcast basis. As suggested in the overall topics graph, some topics are universally or near-universally covered. This includes topics like the Israel-Hamas conflict, TikTok legislation, and the war between Ukraine and Russia. However, some topics are limited to a singular platform. Reuters, for example, is the only podcast that has the Irish Referendum of 2024 as a major topic. Similarly, WSJ is the only podcast where the topic of the Dartmouth Basketball team's planned unionization was identified.

On an individual podcast level, there is noise relating to conversational or otherwise non-relevant dialog contained within the podcast text. This noise includes topics about the hosts or their guests, as seen in Topic 8 in Figure 1.6, or advertisement mentions as seen in Topic 6 in Figure 1.5.

### Sentiment Analysis

For the topic of sentiment analysis, I chose "Israel" since it appeared in all the topic models for the individual podcasts, as well as the overall topic model.  This indicates it was a major  topic of conversation and was covered by all podcasts.

<figure>

<img src="https://i.imgur.com/6gX0x3e.png"/>

<div align="center">

<figcaption>Fig 1.7) Negative Sentiment Over Time By Platform </figcaption>

</div>

</figure>

<figure>

<img src="https://i.imgur.com/7aGUIeX.png"/>

<div align="center">

<figcaption>Fig 1.8) Positive Sentiment Over Time By Platform </figcaption>

</div>

</figure>

<figure>

<img src="https://i.imgur.com/EdKjKm2.png"/>

<div align="center">

<figcaption>Fig 1.9) Neutral Sentiment Over Time By Platform </figcaption>

</div>

</figure>

Figures 1.7-1.9 show the sentiment targeted towards the subject "Israel" over time separated by positive, negative, and neutral values determined by the NewsSentiment model over time. Each podcast has different trends in the sentiment types, but generally, values are highly variable. Neutral tends to be the highest consistent value. There are some notable spikes or drops in sentiment values, notable around March 6th-8th for both Reuters' and Fox's podcasts where negative sentiment spikes. Around the same time, there is a spike in positive sentiment for The Wall Street Journal's podcast.

## Discussion

### Challenges faced with data format and consequences

Very little literature exists on textual podcast analysis, specifically regarding topic and sentiment analysis. The initial idea was that this was due to barriers in converting audio to text, however, after the research process, it is clear other challenges exist in producing high-quality data from podcasts. Podcasts, even formal ones, typically are more conversational and lack the clear distinction for non-relevant content found in traditional media. In traditional media, the advertisements are spatially distinct from relevant news content. In podcasts, once transcribed, there is no consistent component that can be removed or altered to remove extraneous content. Additionally, unlike newspapers, the newscasters sometimes talk about their personal lives or introduce themselves or their guests, which adds more noise to filter through.

The effect of this challenge can be seen in the topic modeling results. The problem is less relevant for overall topic modeling, showing up only as additional noise words in Topic 5 in Figure 1.1. However, it did affect sentence-level topic modeling more for individual podcast analysis. This problem is absent from the overall summary of topics likely because of the additional samples for each day providing a larger document pool, while there is less data available for individual podcasts.

On an individual level, there is only one document per day (daily podcast), and a topic may be relevant for only a short period. While using document-level topic analysis for individual podcasts could capture events that had a long time frame, it failed to capture the same degree of nuance that sentence-level analysis did. Using sentence-level analysis came at the cost of increased noise. Even after some manual sentence removal efforts, some noise persisted in topics like WSJ's Topic 2 or NPR's Topic 1, demonstrating the relevance of the problem.

### Refinement Strategies

One potential solution to reduce noise would be to follow a similar strategy as Vaiani, La Quatra, Cagliero, and Garza (2022) [14]. In this paper, researchers trained a bert-base-cased model to classify if content contained advertising content or not. I attempted to utilize this model for sentence-level detection of advertisement content as it was trained on Spotify podcast data, which was similar to my topic of study. Unfortunately, the model was not sufficiently reliable in detecting advertising content for my specific use case. Furthermore, it was beyond the scope of the model to address the byproducts of casual conversation, which was a large part of the problem as well. As a result of these factors, this processing step was not included.

### Topic analysis

Overall, topic modeling on the entire corpus shows topics that correspond to world events, as well as reflecting other shared trends in reporting.  Topic 0 and 7, which seem to encapsulate rising food prices and electric vehicles fall into this "trend" category. These patterns are not related to one specific event, but rather a general phenomenon that is being reported on by multiple platforms. This  is an  interesting and unexpected result that deviates from the expectation that topics would only correlate with specific events rather than general trends.

In the context of the research question, the individual podcast analysis demonstrates that while there is a large degree of overlap between podcasts on major topics, there are also some more niche topics that are platform-specific. These niche topics may provide insights into platforms' unique reporting priorities and the type of news the podcast aims to provide. For example, the Fox News Rundown is the only podcast that has sports-related topics appearing in its model, which provides information about the informational niche the platform is trying to fill. Additionally, Reuter's World News modeling is unique in that it includes topics like the Irish Referendum or Kate Middleton's illness. This is reasonable given the  scope of reporting for the platform likely extends more beyond the United States than other platforms.

### Sentiment Analysis

The sentiment analysis provides insight into how the different platforms discuss the same topic. The topic chosen as an example for the research was "Israel" given its high frequency of occurrence in the dataset because of the current Israel-Hamas conflict.

There was a spike in negative sentiment around March 6th-8th for both Fox and Reuters, which was unexpected as the platforms generally have differing political views. Upon further examination, they are discussing similar, but not identical topics. Fox's podcast on March 6th and 7th discusses Biden's polling and policies towards Israel. Reuters' podcast on March 7th is discussing a report which alleges that one of their reporters (Isam Adbullah) was killed by an Israeli tank that fired shells into a group of journalists. While these are drastically different causes for negative sentiments, this analysis reveals a shared pattern between the two sources.

## Conclusion

This analysis aimed to create a corpus of news podcasts and understand what topics were discussed, and how to evaluate sentiment on them. These objectives were successfully achieved, as major topics on a general and individual podcast level were identified, and sentiment overtime on a highly covered issue could be evaluated. A major problem was dealing with noise, conversational or advertisement-related, within the dataset.

Future research could expand the corpus in terms of what topics were covered or the period podcasts were collected from. By expanding the sample size, the relevance of noise may decrease. Alternatively, the  utilization of other NLP techniques, such as training a model to detect irrelevant content. Overall, this research provides examples of a potential pipeline to perform NLP analysis on podcast data and demonstrates the relevance of the obtained results.

## References

[1] S. Atske, “Podcasts as a Source of News and Information,” _Pew Research Center’s Journalism Project_, Apr. 18, 2023. https://www.pewresearch.org/journalism/2023/04/18/podcasts-as-a-source-of-news-and-information/ (accessed May 10, 2024).

[2] S. Atske, “A Profile of the Top-Ranked Podcasts in the U.S.,” _Pew Research Center’s Journalism Project_, Jun. 15, 2023. https://www.pewresearch.org/journalism/2023/06/15/a-profile-of-the-top-ranked-podcasts-in-the-u-s/ (accessed May 10, 2024).

[3] A. Fabbri, I. Li, T. She, S. Li, & D. Radev, "Multi-news: a large-scale multi-document summarization dataset and abstractive hierarchical model",, 2019. https://doi.org/10.48550/arxiv.1906.01749

[4] M. Vicari and M. Gáspari, "Analysis of news sentiments using natural language processing and deep learning", AI & SOCIETY, vol. 36, no. 3, p. 931-937, 2020. https://doi.org/10.1007/s00146-020-01111-x

[5] “What’s News - WSJ Podcasts,” _WSJ_. https://www.wsj.com/podcasts/whats-news (accessed May 10, 2024).

[6] NPR, “Up First,” _NPR.org_. https://www.npr.org/podcasts/510318/up-first (accessed May 10, 2024).

[7] Fox News, “FOX News Rundown,” _FOX News Radio_. https://radio.foxnews.com/podcast/fox-news-rundown/ (accessed May 10, 2024).

[8] Reuters, "Reuters World News," *Reuters. https://www.reuters.com/podcasts/ (accessed May 10, 2024).

[9] Wayback Machine,” _web.archive.org_. https://web.archive.org/web/20240000000000*/https://www.wsj.com/podcasts/whats-news

[10] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever, “Robust Speech Recognition via Large-Scale Weak Supervision,” _arXiv:2212.04356 [cs, eess]_, Dec. 2022, Available: https://arxiv.org/abs/2212.04356

[11] M. Grootendorst, “BERTopic: Neural topic modeling with a class-based TF-IDF procedure,” _arXiv (Cornell University)_, Mar. 2022, doi: https://doi.org/10.48550/arxiv.2203.05794.

[12] F. Hamborg and K. Donnay, "Newsmtsc: a dataset for (multi-)target-dependent sentiment classification in political news articles", Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume, 2021. https://doi.org/10.18653/v1/2021.eacl-main.142

[13] “Sentencizer · spaCy API Documentation,” _Sentencizer_. https://spacy.io/api/sentencizer (accessed May 11, 2024).

[14] L. Vaiani, M. La Quatra, L. Cagliero, and P. Garza, “Leveraging Multimodal Content for Podcast Summarization,” _Proceedings of the 37th ACM/SIGAPP Symposium on Applied Computing_, pp. 863–870, Apr. 2022, doi: https://doi.org/10.1145/3477314.3507106.

## Appendices

[GitHub Repository Link](https://github.com/ts2002/nlp-project)

In the root directory, code can be found for topic modeling in TopicCode.ipynb, and the code for sentiment analysis can be found in SentimentAnalysis.ipynb. The .csv dataset used in both notebooks can be found in the root directory of the GitHub repository as well. To run the analysis code, as these notebooks were ran on Google Colab because of local computational limits, it will be necessary to adjust the pd.read_csv path.

The EDA and dataset creation process can be found in EDA.ipynb at the root directory.

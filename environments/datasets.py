# NER_DATASETS = {
#     "ncbi": {
#         "data_dir": "/home/suching/scibert/data/ner/NCBI-disease/",
#     },
#     "sciie": {
#         "data_dir": "/home/suching/scibert/data/ner/sciie/"
#     },
#     "jnlpba": {
#         "data_dir": "/home/suching/scibert/data/ner/JNLPBA/"
#     },
#     "bc5cdr": {
#         "data_dir": "/home/suching/scibert/data/ner/bc5cdr/"
#     }
# }


# CLASSIFICATION_DATASETS = {
#     "hatespeech": {
#         "data_dir": "s3://suching-dev/textcat/twitter/hatespeech/",
#     },
#     "ag": {
#         "data_dir": "s3://suching-dev/textcat/news/ag/"
#     },
#     "scicite": {
#         "data_dir": "s3://suching-dev/textcat/science/sci-cite/",
#     },
#     "citation_intent": {
#         "data_dir": "s3://suching-dev/textcat/science/citation_intent/"
#     },
#     "chemprot": {
#         "data_dir": "s3://suching-dev/textcat/science/chemprot/"
#     },
#     "sciie": {
#         "data_dir": "s3://suching-dev/textcat/science/sciie/",
#     },
#     "hyperpartisan_news": {
#         "data_dir": "s3://suching-dev/textcat/news/hyperpartisan_by_article/",
#     },
#     "biased_news": {
#         "data_dir": "s3://suching-dev/textcat/news/biased_news/",
#     },
#     "imdb": {
#         "data_dir": "s3://suching-dev/textcat/reviews/imdb/",
#     },
#     "amazon": {
#         "data_dir": "s3://suching-dev/textcat/reviews/amazon/",
#     },
#     "yelp": {
#         "data_dir": "s3://suching-dev/textcat/reviews/yelp/",
#     },
#     "twitter_sentiment": {
#         "data_dir": "s3://suching-dev/textcat/twitter/semeval_2017_ task_4A/",
#     },
#     "twitter_irony_task_a": {
#         "data_dir": "s3://suching-dev/textcat/twitter/semeval_2018_task3_irony_detection/task_a/",
#     },
#     "twitter_irony_task_b": {
#         "data_dir": "s3://suching-dev/textcat/twitter/semeval_2018_task3_irony_detection/task_b/",
#     },
#     "rct-20k": {
#         "data_dir": "s3://suching-dev/textcat/science/rct-20k/",
#     },
#     "cs-abstruct": {
#         "data_dir": "s3://suching-dev/textcat/science/csabstruct-reformat/",
#     }
# }


# DATASETS = {"NER": NER_DATASETS, "CLASSIFICATION": CLASSIFICATION_DATASETS}
NER_DATASETS = {
    "ncbi": {
        "data_dir": "/home/suching/scibert/data/ner/NCBI-disease/",
    },
    "sciie": {
        "data_dir": "/home/suching/scibert/data/ner/sciie/"
    },
    "jnlpba": {
        "data_dir": "/home/suching/scibert/data/ner/JNLPBA/"
    },
    "bc5cdr": {
        "data_dir": "/home/suching/scibert/data/ner/bc5cdr/"
    }
}



CLASSIFICATION_DATASETS = {
    "chemprot": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/chemprot/",
        "dataset_size": 4169
    },
    "rct-20k": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/rct-20k/",
        "dataset_size": 180040
    },
    "rct-sample": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/rct-sample/",
        "dataset_size": 500
    },
    "citation_intent": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/citation_intent/",
        "dataset_size": 1688
    },
    "sciie": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/sciie/",
        "dataset_size": 3219
    },
    "ag": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/ag/",
        "dataset_size": 115000
    },
    "hyperpartisan_news": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/hyperpartisan_news/",
        "dataset_size": 500
    },
    "imdb": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/imdb/",
        "dataset_size": 20000
    },
    "amazon": {
        "data_dir": "https://s3-us-west-2.amazonaws.com/allennlp/dont_stop_pretraining/data/amazon/",
        "dataset_size": 115251
    }
}


DATASETS = {"NER": NER_DATASETS, "CLASSIFICATION": CLASSIFICATION_DATASETS}
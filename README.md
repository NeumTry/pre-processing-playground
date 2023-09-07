# Pre-processing playground

To use the hosted app, head to [https://neumai-playground.streamlit.app/](https://neumai-playground.streamlit.app/)
Project is a fork of the [Langchain Text Splitter Explorer](https://github.com/langchain-ai/text-split-explorer). 

At [Neum AI](https://neum.ai), we are focused on building the next generation of data pipelines built specifically for embeddings and RAG.
Preparing data to be converted into vector embeddings and ingested in vector databases is challening.
Different data types have different requirements and best practices to best convert them and optimize them for retrieval.


Starting with choosing the right loader that will correctly extract the text and format from the original file.
For structured data types like JSON and CSVs, separating the content that is worth embeddings and the content that should just serve as metadata is necessary.
Once we have the text that contains our context, it must be split into smaller chunks while mantaining a cohesive information structure. - e.g. you don't just want to split in the middle of sentence.
Chunking can take different shapes and forms depending on the type of document it is.
For example for a Q&A document you want to keep Q&As together. If the document is report with sections, you want to keep the sections together. If it is code, you want to keep classes and methods together.

## What can the app do?

Using this repo and the associated app, you can test pre-processing flows for different documents.
It is likely that you might be processing documents that generally follow a similar structure, so optimizing your process can help you apply it across your document set.
The app allows you to upload a file, choose the loader you want to use and the splitter to chunk it.
In addition, you can leverage metadata selectors to attach metadata to the resulting chunks. (only available for JSONs and CSVs using the provided loaders).
**The app does not store any data, simply uploads to temp storage to use at runtime and then cleans up.**

## What is coming?

We will be adding more capabilities to the app to further match the feature set that we offer through Neum AI. 
This inlcudes intelligence layers to pick the correct loaders, chunkers, etc. 
As well as more nuanced loaders and chunkers that are specific to a given data type as well as document context. (ex. reports, Q&A, contracts, etc.)
**To learn more or collaborate email: founders@tryneum.com**

## Running locally

To run locally, first set up the environment by cloning the repo and running:

```shell
pip install -r requirements
```

Then, run the Streamlit app with:

```shell
streamlit run splitter.py
```

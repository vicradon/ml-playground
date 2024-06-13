# Product Recommendation Pipeline with Argo Workflows

This project is a demo of how one can implement product recommendations in a workflow-like engine (like Argo Workflows). The purpose of this workflow is to build a machine-learning pipeline that recommends products based on images in the object storage container and user queries. The steps of the workflow include:

1. Preprocess - prepare the data for training
2. Register - set up a new task on the training pipeline
3. Train - run the training pipeline with VGG16 for cosine similarity
4. Deploy - push the trained model to production. In this case, the storage container with the models and trigger a restart of the product recommendation service


docker build src/preprocess -t vicradon/recommender-preprocess
docker build src/train -t vicradon/recommender-preprocess
docker build src/register -t vicradon/recommender-preprocess

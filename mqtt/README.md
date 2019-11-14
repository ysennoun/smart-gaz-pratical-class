docker-compose build
docker-compose up
docker-compose down
docker exec -it consumer bash
docker exec -it publisher bash
docker-compose logs publisher

localhost:5601

curl -X POST "es02:9200/twitter/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
    "user" : "kimchy",
    "post_date" : "2019-11-16T10:10:12",
    "message" : "trying out Elasticsearch"
}
'


gaz parfait hélium
P.V = n.R.T
https://industrie.airliquide.fr/sites/industry_fr/files/2016/06/24/gamme-bouteilles_air-liquide-france-industrie_4310879549933597796.pdf
https://fr.wikipedia.org/wiki/Gaz_parfait
V=50L
P=200Bar
R = 8,314 462 1 J K−1 mol−1
T= 25°C

coap application https://fr.wikipedia.org/wiki/CoAP#Impl%C3%A9mentations_et_Applications_pratiques


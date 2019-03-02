from django.shortcuts import render

# Create your views here.
def home(request):
    json_data = [
			  {
			    "crop_id": 1,
			    "crop": "Rice",
			    "rainfall": "100-150",
			    "temperature": "15-27",
			    "soil": "heavy-clayeyÿ",
			    "Description": "Rice is the seed of the grass species Oryza sativa or Oryza glaberrima. As a cereal grain, it is the most widely consumed staple food for a large part of the world's human population, especially in Asia. It is the agricultural commodity with the third-highest worldwide production, after sugarcane and maize",
			    "Harvest_Days": 120,
			    "image_URL": "https://static01.nyt.com/images/2018/02/21/dining/00RICEGUIDE8/00RICEGUIDE8-threeByTwoMediumAt2X.jpg"
			  },
			  {
			    "crop_id": 2,
			    "crop": "Wheat",
			    "rainfall": "25-75",
			    "temperature": "13-25",
			    "soil": "well-drained-light clayÿ",
			    "Description": "Wheat is a grass widely cultivated for its seed, a cereal grain which is a worldwide staple food. The many species of wheat together make up the genus Triticum; the most widely grown is common wheat",
			    "Harvest_Days": 90,
			    "image_URL": "https://5.imimg.com/data5/KY/SY/MY-17256771/wheat-500x500.jpg"
			  },
			  {
			    "crop_id": 3,
			    "crop": "Maize",
			    "rainfall": "65-125",
			    "temperature": "15-27",
			    "soil": "deep-heavy clay",
			    "Description": "Maize, also known as corn, is a cereal grain first domesticated by indigenous peoples in southern Mexico about 10,000 years ago. The leafy stalk of the plant produces pollen inflorescences and separate ovuliferous inflorescences called ears that yield kernels or seeds, which are fruits",
			    "Harvest_Days": 90,
			    "image_URL": "https://5.imimg.com/data5/TB/DM/MY-49495609/maize-2f-corn-28yellow-29-500x500.jpg"
			  },
			  {
			    "crop_id": 4,
			    "crop": "Millets",
			    "rainfall": "25-75",
			    "temperature": "20-35",
			    "soil": "Sandy-loam",
			    "Description": "Millets are a group of highly variable small-seeded grasses, widely grown around the world as cereal crops or grains for fodder and human food. Millets are important crops in the semiarid tropics of Asia and Africa, with 97% of millet production in developing countries",
			    "Harvest_Days": 120,
			    "image_URL": "https://5.imimg.com/data5/JV/RE/MY-48933929/foxtail-millet-500x500.png"
			  },
			  {
			    "crop_id": 5,
			    "crop": "Bajra",
			    "rainfall": "25-60",
			    "temperature": "25-35",
			    "soil": "Sandy loam",
			    "Description": "Bajra is a coarse grain crop and considered to be the poor man's staple nourishment and suitable to cultivate in dry lands. Major Bajra production states in India are: Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat.",
			    "Harvest_Days": 90,
			    "image_URL": "http://tajagroproducts.com/images/Green%20Bajra/greeb%20bajara.jpg"
			  },
			  {
			    "crop_id": 6,
			    "crop": "Pulses",
			    "rainfall": "25-60",
			    "temperature": "20-27",
			    "soil": "Sandy-loam",
			    "Description": "Pulses are the edible seeds of plants in the legume family. Pulses grow in pods and come in a variety of shapes, sizes and colors. The United Nations Food and Agriculture Organization (FAO) recognizes 11 types of pulses: dry beans, dry broad beans, dry peas, chickpeas, cow peas, pigeon peas, lentils, Bambara beans, vetches, lupins and pulses nes",
			    "Harvest_Days": 90,
			    "image_URL": "http://farmersmarketsnovascotia.com/wp-content/uploads/2016/03/Pulses.jpg"
			  },
			  {
			    "crop_id": 7,
			    "crop": "Lentil",
			    "rainfall": "25-50",
			    "temperature": "15-25",
			    "soil": "clayey loam",
			    "Description": "The lentil (Lens culinaris or Lens esculenta) is an edible legume. It is a bushy annual plant known for its lens-shaped seeds. It is about 40 cm (16 in) tall, and the seeds grow in pods, usually with two seeds in each. In South Asian cuisine, split lentils (often with their hulls removed) are known as dal",
			    "Harvest_Days": 90,
			    "image_URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/3_types_of_lentil.jpg/1200px-3_types_of_lentil.jpg"
			  },
			  {
			    "crop_id": 8,
			    "crop": "Oilseeds",
			    "rainfall": "30-50",
			    "temperature": "15-30",
			    "soil": "clayey loam",
			    "Description": "Oil seeds, also known as rape, oilseed rape, and, in the case of one particular group of cultivars, canola, is a bright-yellow flowering member of the family Brassicaceae, cultivated mainly for its oil-rich seed. It is the third-largest source of vegetable oil in the world",
			    "Harvest_Days": 95,
			    "image_URL": "https://indolinkenglish.files.wordpress.com/2011/05/oilseeds.jpg"
			  },
			  {
			    "crop_id": 9,
			    "crop": "Groundnut",
			    "rainfall": "50-75",
			    "temperature": "20-30",
			    "soil": "well-drained-sandy loams",
			    "Description": "Groundnut also known as the groundnut, goober, or monkey nut, and taxonomically classified as Arachis hypogaea, is a legume crop grown mainly for its edible seeds. It is widely grown in the tropics and subtropics, being important to both small and large commercial producers",
			    "Harvest_Days": 120,
			    "image_URL": "http://buzznigeria.com/wp-content/uploads/2016/02/groundnut2.jpg"
			  },
			  {
			    "crop_id": 10,
			    "crop": "Sugarcane",
			    "rainfall": "85-165",
			    "temperature": "50-75",
			    "soil": "Well-drained alluvium",
			    "Description": "Sugarcane, or sugar cane, are several species of tall perennial true grasses of the genus Saccharum, tribe Andropogoneae, native to the warm temperate to tropical regions of South, Southeast Asia, and New Guinea, and used for sugar production.",
			    "Harvest_Days": 60,
			    "image_URL": "https://tamilandvedas.files.wordpress.com/2014/08/sugar-cane-plantation.jpg"
			  },
			  {
			    "crop_id": 11,
			    "crop": "Sugar beet",
			    "rainfall": "25-50",
			    "temperature": "10-25",
			    "soil": "Well-drained-loamy soil",
			    "Description": "A sugar beet is a plant whose root contains a high concentration of sucrose and which is grown commercially for sugar production. In plant breeding it is known as the Altissima cultivar group of the common beet.",
			    "Harvest_Days": 50,
			    "image_URL": "https://www.greencoverseed.com/wordpress/wp-content/uploads/2017/04/sugarbeets.jpg"
			  },
			  {
			    "crop_id": 12,
			    "crop": "Cotton",
			    "rainfall": "60-110",
			    "temperature": "18-27",
			    "soil": "well-drained loam",
			    "Description": "Cotton is a soft, fluffy staple fiber that grows in a boll, or protective case, around the seeds of the cotton plants of the genus Gossypium in the mallow family Malvaceae. The fiber is almost pure cellulose. Under natural conditions, the cotton bolls will increase the dispersal of the seeds",
			    "Harvest_Days": 150,
			    "image_URL": "https://i2.wp.com/altenewblog.com/wp-content/uploads/2014/12/img_0710.jpg"
			  },
			  {
			    "crop_id": 13,
			    "crop": "Tea",
			    "rainfall": "100-250",
			    "temperature": "15-35",
			    "soil": "light loamy Soil",
			    "Description": "Tea is an aromatic beverage commonly prepared by pouring hot or boiling water over cured leaves of the Camellia sinensis, an evergreen shrub (bush) native to East Asia.[3] After water, it is the most widely consumed drink in the world. There are many different types of tea; some, like Darjeeling and Chinese greens, have a cooling, slightly bitter, and astringent flavour,[5] while others have vastly different profiles that include sweet, nutty, floral or grassy notes",
			    "Harvest_Days": 180,
			    "image_URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Csinensis.jpg/1200px-Csinensis.jpg"
			  },
			  {
			    "crop_id": 14,
			    "crop": "Coffee",
			    "rainfall": "125-225",
			    "temperature": "15-28",
			    "soil": "well-drained alluvial Soil",
			    "Description": "Coffea is a genus of flowering plants in the family Rubiaceae. Coffea species are shrubs or small trees native to tropical and southern Africa and tropical Asia. The seeds of some species, called coffee beans, are used to make various coffee beverages and products",
			    "Harvest_Days": 85,
			    "image_URL": "https://plantslive.in/wp-content/uploads/2017/10/coffee-plant.jpg"
			  },
			  {
			    "crop_id": 15,
			    "crop": "Cocoa",
			    "rainfall": "100-250",
			    "temperature": "18-35",
			    "soil": "well-drained alluvium",
			    "Description": "The cocoa bean or simply cocoa, which is also called the cacao bean or cacao , is the dried and fully fermented seed of Theobroma cacao, from which cocoa solids (a mixture of nonfat substances) and cocoa butter (the fat) can be extracted. Cocoa beans are the basis of chocolate, and Mesoamerican foods including tejate, a pre-Hispanic drink that also includes maize.",
			    "Harvest_Days": 150,
			    "image_URL": "https://www.omanhene.com/wp-content/uploads/Rethink.png"
			  },
			  {
			    "crop_id": 16,
			    "crop": "Rubber",
			    "rainfall": "150-250",
			    "temperature": 27,
			    "soil": "well-drained alluvial Soilÿ",
			    "Description": "Natural rubber, also called India rubber or caoutchouc, as initially produced, consists of polymers of the organic compound isoprene, with minor impurities of other organic compounds, plus water. Thailand and Indonesia are two of the leading rubber producers.",
			    "Harvest_Days": 200,
			    "image_URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Latex_-_Hevea_-_Cameroun.JPG/1200px-Latex_-_Hevea_-_Cameroun.JPG"
			  },
			  {
			    "crop_id": 17,
			    "crop": "Jute",
			    "rainfall": "150-250",
			    "temperature": "25-35",
			    "soil": "Well drained alluvial Soil",
			    "Description": "Jute is a long, soft, shiny vegetable fiber that can be spun into coarse, strong threads. It is produced primarily from plants in the genus Corchorus, which was once classified with the family Tiliaceae, and more recently with Malvaceae",
			    "Harvest_Days": 75,
			    "image_URL": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Jute_Rope_%28%E0%AE%9A%E0%AE%A3%E0%AE%B2%E0%AF%8D_%E0%AE%95%E0%AE%AF%E0%AE%BF%E0%AE%B1%E0%AF%81%29.jpg/220px-Jute_Rope_%28%E0%AE%9A%E0%AE%A3%E0%AE%B2%E0%AF%8D_%E0%AE%95%E0%AE%AF%E0%AE%BF%E0%AE%B1%E0%AF%81%29.jpg"
			  },
			  {
			    "crop_id": 18,
			    "crop": "Flax",
			    "rainfall": "15-20",
			    "temperature": "10-20",
			    "soil": "clayey loam",
			    "Description": "Flax, also known as common flax or linseed, is a member of the genus Linum in the family Linaceae. It is a food and fiber crop cultivated in cooler regions of the world. The textiles made from flax are known in the Western countries as linen, and traditionally used for bed sheets, underclothes, and table linen",
			    "Harvest_Days": 85,
			    "image_URL": "https://4.imimg.com/data4/ED/JM/MY-22972899/flax-seeds-alsi-500x500.jpg"
			  },
			  {
			    "crop_id": 19,
			    "crop": "Coconut",
			    "rainfall": "100-250",
			    "temperature": 27,
			    "soil": "sandy alluvial sandy",
			    "Description": "The coconut tree is a member of the palm tree family and the only living species of the genus Cocos. The term \"coconut\" can refer to the whole coconut palm, the seed, or the fruit, which botanically is a drupe, not a nut.",
			    "Harvest_Days": 30,
			    "image_URL": "https://thecoconutmama.com/wp-content/uploads/2018/01/coconut.png"
			  },
			  {
			    "crop_id": 20,
			    "crop": "Oil-palm",
			    "rainfall": "250-400",
			    "temperature": "22-33",
			    "soil": "alluvial soil",
			    "Description": "Palm oil is an edible vegetable oil derived from the mesocarp of the fruit of the oil palms, primarily the African oil palm Elaeis guineensis, and to a lesser extent from the American oil palm Elaeis oleifera and the maripa palm Attalea maripa",
			    "Harvest_Days": 70,
			    "image_URL": "http://oilpalmindia.com/wp-content/uploads/2015/09/oilpalmtree.jpg"
			  },
			  {
			    "crop_id": 21,
			    "crop": "Clove",
			    "rainfall": "200-250",
			    "temperature": "25-35",
			    "soil": "Red alluvial Soilÿÿÿÿ",
			    "Description": "Cloves are the aromatic flower buds of a tree in the family Myrtaceae, Syzygium aromaticum. They are native to the Maluku Islands in Indonesia, and are commonly used as a spice. Cloves are commercially harvested primarily in Bangladesh, Indonesia, India, Madagascar, Pakistan, Sri Lanka, and Tanzania",
			    "Harvest_Days": 60,
			    "image_URL": "https://images-na.ssl-images-amazon.com/images/I/810Ypf0P4oL._SY355_.jpg"
			  },
			  {
			    "crop_id": 22,
			    "crop": "Black Pepper",
			    "rainfall": "200-300",
			    "temperature": "15-40",
			    "soil": "red-loam",
			    "Description": "Piper nigrum is a flowering vine in the family Piperaceae, cultivated for its fruit, which is usually dried and used as a spice and seasoning, known as a peppercorn. When fresh and fully mature, it is about 5 mm in diameter and dark red, and contains a single seed, like all drupes.",
			    "Harvest_Days": 75,
			    "image_URL": "https://static.thespicehouse.com/images/file/518/large_square_Lampong_Indonesian_Black_Peppercorns__close.jpg"
			  },
			  {
			    "crop_id": 23,
			    "crop": "Cardamon",
			    "rainfall": "150-400",
			    "temperature": "10-35",
			    "soil": "well-drained lateritic",
			    "Description": "Cardamom, sometimes cardamon or cardamum, is a spice made from the seeds of several plants in the genera Elettaria and Amomum in the family Zingiberaceae. Both genera are native to the Indian subcontinent and Indonesia",
			    "Harvest_Days": 30,
			    "image_URL": "https://static.thespicehouse.com/images/file/281/large_square_Green_Cardamom__Whole_Fancy_Pods__close.jpg"
			  },
			  {
			    "crop_id": 24,
			    "crop": "Turmeric",
			    "rainfall": "150-250",
			    "temperature": "20-30",
			    "soil": "well-drained clayey loam or red loamy soilÿÿ",
			    "Description": "Turmeric is a flowering plant of the ginger family, Zingiberaceae, the roots of which are used in cooking.",
			    "Harvest_Days": 60,
			    "image_URL": "https://cdn1.medicalnewstoday.com/content/images/articles/318/318739/turmeric-root-and-powder.jpg"
			  }
			]
    args = {}
    args['contents'] = json_data
    return render(request, 'home/library.html',args)
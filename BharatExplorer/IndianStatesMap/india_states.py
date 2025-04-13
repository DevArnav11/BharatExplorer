# Data for Indian states, union territories and monuments including coordinates, details, and image URLs

famous_monuments = [
    {
        "name": "Taj Mahal",
        "latitude": 27.1751,
        "longitude": 78.0421,
        "state": "Uttar Pradesh",
        "details": "One of the Seven Wonders of the World, built by Shah Jahan in memory of his wife Mumtaz Mahal",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Taj_Mahal%2C_Agra%2C_India_edit2.jpg/320px-Taj_Mahal%2C_Agra%2C_India_edit2.jpg",
        "google_maps": "https://goo.gl/maps/5yqHXD8KqvTKKwvK7"
    },
    {
        "name": "Red Fort",
        "latitude": 28.6562,
        "longitude": 77.2410,
        "state": "Delhi",
        "details": "Historic fortress built in the 17th century by Mughal Emperor Shah Jahan",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Delhi_Red_fort.jpg/320px-Delhi_Red_fort.jpg",
        "google_maps": "https://goo.gl/maps/zUmB4q8AAugy5G4P8"
    },
    {
        "name": "Ajanta Caves",
        "latitude": 20.5519,
        "longitude": 75.7033,
        "state": "Maharashtra",
        "details": "Ancient Buddhist caves with remarkable paintings and rock-cut architecture dating from 2nd century BCE",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Ajanta_Caves%2C_Aurangabad_tr.jpg/320px-Ajanta_Caves%2C_Aurangabad_tr.jpg",
        "google_maps": "https://goo.gl/maps/jsJ8yqGYBxQKpDZq5"
    },
    {
        "name": "Khajuraho Temples",
        "latitude": 24.8318,
        "longitude": 79.9199,
        "state": "Madhya Pradesh",
        "details": "Famous for their Nagara-style architectural symbolism and erotic sculptures from the Chandela period",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Khajuraho_-_Kandariya_Mahadeva_Temple.jpg/320px-Khajuraho_-_Kandariya_Mahadeva_Temple.jpg",
        "google_maps": "https://goo.gl/maps/gW1YH5S3jE6dvrhw7"
    },
    {
        "name": "Sanchi Stupa",
        "latitude": 23.4791,
        "longitude": 77.7375,
        "state": "Madhya Pradesh",
        "details": "Oldest stone structure in India commissioned by Emperor Ashoka in the 3rd century BCE",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Sanchi_Stupa.jpg/320px-Sanchi_Stupa.jpg",
        "google_maps": "https://goo.gl/maps/YxKLWXGkMHtqzaK89"
    },
    {
        "name": "Konark Sun Temple",
        "latitude": 19.8876,
        "longitude": 86.0945,
        "state": "Odisha",
        "details": "13th-century Sun Temple known for its intricate architecture and massive chariot wheels",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Konarak_Temple.jpg/320px-Konarak_Temple.jpg",
        "google_maps": "https://goo.gl/maps/NaSjr6nPP8Yf5ZXFA"
    },
    {
        "name": "Hampi Monuments",
        "latitude": 15.3350,
        "longitude": 76.4600,
        "state": "Karnataka",
        "details": "UNESCO World Heritage site featuring ruins of the Vijayanagara Empire",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Hampi_Virupaksha_Temple.jpg/320px-Hampi_Virupaksha_Temple.jpg",
        "google_maps": "https://goo.gl/maps/R5tJ5htQRmkM9WDZA"
    },
    {
        "name": "Qutub Minar",
        "latitude": 28.5245,
        "longitude": 77.1855,
        "state": "Delhi",
        "details": "UNESCO World Heritage site, built in the early 13th century by the first ruler of Delhi Sultanate",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Qutub_Minar%2C_Delhi.jpg/320px-Qutub_Minar%2C_Delhi.jpg",
        "google_maps": "https://goo.gl/maps/y1fKxKxpYCmHbYVL9"
    },
    {
        "name": "Fatehpur Sikri",
        "latitude": 27.0944,
        "longitude": 77.6695,
        "state": "Uttar Pradesh",
        "details": "Ancient city built by Mughal Emperor Akbar, featuring stunning Indo-Islamic architecture",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Fatehpur_Sikri_Palace.jpg/320px-Fatehpur_Sikri_Palace.jpg",
        "google_maps": "https://goo.gl/maps/HFzqt8HuWHxPKurv6"
    },
    {
        "name": "Elephanta Caves",
        "latitude": 18.9633,
        "longitude": 72.9315,
        "state": "Maharashtra",
        "details": "Ancient cave temples dedicated to Lord Shiva, located on Elephanta Island near Mumbai",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Elephanta_Caves.jpg/320px-Elephanta_Caves.jpg",
        "google_maps": "https://goo.gl/maps/DP5mZEhZHP4k7Sxx8"
    }
]
# Also includes major cities and landmarks for search functionality
india_states = [
    # States
    {
        "name": "Andhra Pradesh",
        "latitude": 16.5062,
        "longitude": 80.6480,
        "famous_for": "Tirupati Temple and Andhra Pickles",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Tirumala_090615.jpg/320px-Tirumala_090615.jpg",
        "type": "state",
        "capital": "Amaravati",
        "major_cities": ["Visakhapatnam", "Vijayawada", "Tirupati", "Guntur", "Nellore"],
        "landmarks": ["Tirupati Temple", "Araku Valley", "Borra Caves", "Lepakshi Temple"]
    },
    {
        "name": "Arunachal Pradesh",
        "latitude": 27.1004,
        "longitude": 93.6168,
        "famous_for": "Tawang Monastery and Ziro Valley",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Tawang_Monastery_Arunachal_Pradesh.jpg/320px-Tawang_Monastery_Arunachal_Pradesh.jpg",
        "type": "state",
        "capital": "Itanagar",
        "major_cities": ["Itanagar", "Tawang", "Naharlagun", "Pasighat", "Along"],
        "landmarks": ["Tawang Monastery", "Ziro Valley", "Sela Pass", "Namdapha National Park"]
    },
    {
        "name": "Assam",
        "latitude": 26.1433,
        "longitude": 91.7898,
        "famous_for": "Kaziranga National Park and Assam Tea",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/One_horned_rhinoceros_%28Rhinoceros_unicornis%29.jpg/320px-One_horned_rhinoceros_%28Rhinoceros_unicornis%29.jpg",
        "type": "state",
        "capital": "Dispur",
        "major_cities": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Nagaon"],
        "landmarks": ["Kaziranga National Park", "Kamakhya Temple", "Majuli Island"]
    },
    {
        "name": "Bihar",
        "latitude": 25.0961,
        "longitude": 85.3131,
        "famous_for": "Bodh Gaya and Litti Chokha",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Mahabodhi_Temple_2.jpg/320px-Mahabodhi_Temple_2.jpg"
    },
    {
        "name": "Chhattisgarh",
        "latitude": 21.2787,
        "longitude": 81.8661,
        "famous_for": "Chitrakote Falls and Bastar Art",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Chitrakote_Falls.jpg/320px-Chitrakote_Falls.jpg"
    },
    {
        "name": "Goa",
        "latitude": 15.2993,
        "longitude": 74.1240,
        "famous_for": "Beaches and Seafood",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Goa_North_view.jpg/320px-Goa_North_view.jpg"
    },
    {
        "name": "Gujarat",
        "latitude": 23.0225,
        "longitude": 72.5714,
        "famous_for": "Statue of Unity and Dhokla",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Statue_of_Unity_in_2018.jpg/320px-Statue_of_Unity_in_2018.jpg"
    },
    {
        "name": "Haryana",
        "latitude": 29.0588,
        "longitude": 76.0856,
        "famous_for": "Kurukshetra and Butter Milk",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Brahma_Sarovar.JPG/320px-Brahma_Sarovar.JPG"
    },
    {
        "name": "Himachal Pradesh",
        "latitude": 31.1048,
        "longitude": 77.1734,
        "famous_for": "Shimla and Apple Orchards",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/India_Shimla_Christ_Church_IMG_2071a.jpg/320px-India_Shimla_Christ_Church_IMG_2071a.jpg"
    },
    {
        "name": "Jharkhand",
        "latitude": 23.6102,
        "longitude": 85.2799,
        "famous_for": "Betla National Park and Tribal Culture",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Betla_Forest_National_Park_Jharkhand.jpg/320px-Betla_Forest_National_Park_Jharkhand.jpg"
    },
    {
        "name": "Karnataka",
        "latitude": 12.9716,
        "longitude": 77.5946,
        "famous_for": "Mysore Palace and Bisi Bele Bath",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Mysore_Palace_Morning.jpg/320px-Mysore_Palace_Morning.jpg"
    },
    {
        "name": "Kerala",
        "latitude": 9.9312,
        "longitude": 76.2673,
        "famous_for": "Backwaters and Sadya",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Houseboats_in_Kumarakom_%2C_Kottayam%2CKerala.jpg/320px-Houseboats_in_Kumarakom_%2C_Kottayam%2CKerala.jpg"
    },
    {
        "name": "Madhya Pradesh",
        "latitude": 23.2599,
        "longitude": 77.4126,
        "famous_for": "Khajuraho Temples and Poha",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Khajuraho-Vishvanath_Temple.jpg/320px-Khajuraho-Vishvanath_Temple.jpg"
    },
    {
        "name": "Maharashtra",
        "latitude": 19.0760,
        "longitude": 72.8777,
        "famous_for": "Gateway of India and Vada Pav",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Mumbai_-_Gateway_of_India2.JPG/320px-Mumbai_-_Gateway_of_India2.JPG",
        "type": "state",
        "capital": "Mumbai",
        "major_cities": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
        "landmarks": ["Gateway of India", "Ajanta Caves", "Ellora Caves", "Shivaji Terminus"]
    },
    {
        "name": "Manipur",
        "latitude": 24.8170,
        "longitude": 93.9368,
        "famous_for": "Loktak Lake and Manipuri Dance",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Loktak_Lake.jpg/320px-Loktak_Lake.jpg"
    },
    {
        "name": "Meghalaya",
        "latitude": 25.5788,
        "longitude": 91.8933,
        "famous_for": "Living Root Bridges and Cherrapunji",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Living_root_bridge.jpg/320px-Living_root_bridge.jpg"
    },
    {
        "name": "Mizoram",
        "latitude": 23.1645,
        "longitude": 92.9376,
        "famous_for": "Bamboo Dance and Blue Mountains",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Phawngpui_Blue_Mountain_National_Park.jpg/320px-Phawngpui_Blue_Mountain_National_Park.jpg"
    },
    {
        "name": "Nagaland",
        "latitude": 26.1584,
        "longitude": 94.5624,
        "famous_for": "Hornbill Festival and Kohima War Cemetery",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Khonoma_Community.jpg/320px-Khonoma_Community.jpg"
    },
    {
        "name": "Odisha",
        "latitude": 20.2961,
        "longitude": 85.8245,
        "famous_for": "Konark Sun Temple and Puri Jagannath Temple",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Konarak_Temple.jpg/320px-Konarak_Temple.jpg"
    },
    {
        "name": "Punjab",
        "latitude": 31.1471,
        "longitude": 75.3412,
        "famous_for": "Golden Temple and Butter Chicken",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/The_Golden_Temple_of_Amritsar%2C_Punjab%2C_India_%281%29.jpg/320px-The_Golden_Temple_of_Amritsar%2C_Punjab%2C_India_%281%29.jpg"
    },
    {
        "name": "Rajasthan",
        "latitude": 26.9124,
        "longitude": 75.7873,
        "famous_for": "Jaipur Pink City and Dal Baati Churma",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/The_Hawa_Mahal.jpg/320px-The_Hawa_Mahal.jpg"
    },
    {
        "name": "Sikkim",
        "latitude": 27.5330,
        "longitude": 88.5122,
        "famous_for": "Kanchenjunga and Momos",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Kangchenjunga.jpg/320px-Kangchenjunga.jpg"
    },
    {
        "name": "Tamil Nadu",
        "latitude": 13.0827,
        "longitude": 80.2707,
        "famous_for": "Meenakshi Temple and Dosa",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Madurai_Meenakshi_Amman_Temple.jpg/320px-Madurai_Meenakshi_Amman_Temple.jpg"
    },
    {
        "name": "Telangana",
        "latitude": 17.3850,
        "longitude": 78.4867,
        "famous_for": "Charminar and Hyderabadi Biryani",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Charminar-Pride_of_Hyderabad.jpg/320px-Charminar-Pride_of_Hyderabad.jpg"
    },
    {
        "name": "Tripura",
        "latitude": 23.9408,
        "longitude": 91.9882,
        "famous_for": "Neermahal Palace and Tribal Culture",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Neermahal_Water_Palace.jpg/320px-Neermahal_Water_Palace.jpg"
    },
    {
        "name": "Uttar Pradesh",
        "latitude": 27.1751,
        "longitude": 78.0421,
        "famous_for": "Taj Mahal and Petha",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Taj_Mahal%2C_Agra%2C_India_edit2.jpg/320px-Taj_Mahal%2C_Agra%2C_India_edit2.jpg"
    },
    {
        "name": "Uttarakhand",
        "latitude": 30.0668,
        "longitude": 79.0193,
        "famous_for": "Rishikesh and Valley of Flowers",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Rishikesh_Aerial.jpg/320px-Rishikesh_Aerial.jpg"
    },
    {
        "name": "West Bengal",
        "latitude": 22.5726,
        "longitude": 88.3639,
        "famous_for": "Victoria Memorial and Rasgulla",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Victoria_Memorial_Morning.jpg/320px-Victoria_Memorial_Morning.jpg"
    },
    
    # Union Territories
    {
        "name": "Andaman and Nicobar Islands",
        "latitude": 11.7401,
        "longitude": 92.6586,
        "famous_for": "Cellular Jail and Radhanagar Beach",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/CellularJailfront.jpg/320px-CellularJailfront.jpg",
        "type": "union_territory"
    },
    {
        "name": "Chandigarh",
        "latitude": 30.7333,
        "longitude": 76.7794,
        "famous_for": "Rock Garden and Sukhna Lake",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Chandigarh_Rock_Garden_025.jpg/320px-Chandigarh_Rock_Garden_025.jpg",
        "type": "union_territory"
    },
    {
        "name": "Dadra and Nagar Haveli and Daman & Diu",
        "latitude": 20.1809,
        "longitude": 73.0169,
        "famous_for": "Portuguese Architecture and Beaches",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Fort_of_Moti_Daman.JPG/320px-Fort_of_Moti_Daman.JPG",
        "type": "union_territory"
    },
    {
        "name": "Delhi",
        "latitude": 28.6139,
        "longitude": 77.2090,
        "famous_for": "Red Fort and Delhi Street Food",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Delhi_Red_fort.jpg/320px-Delhi_Red_fort.jpg",
        "type": "union_territory",
        "capital": "New Delhi",
        "major_cities": ["New Delhi", "Delhi", "Dwarka", "Rohini", "Pitampura"],
        "landmarks": ["Red Fort", "India Gate", "Qutub Minar", "Humayun's Tomb", "Lotus Temple"]
    },
    {
        "name": "Jammu and Kashmir",
        "latitude": 34.0837,
        "longitude": 74.7973,
        "famous_for": "Dal Lake and Gulmarg",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Dal_Lake_Srinagar.jpg/320px-Dal_Lake_Srinagar.jpg",
        "type": "union_territory"
    },
    {
        "name": "Ladakh",
        "latitude": 34.1526,
        "longitude": 77.5770,
        "famous_for": "Pangong Lake and Monasteries",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Pangong_Tso_Lake_India.jpg/320px-Pangong_Tso_Lake_India.jpg",
        "type": "union_territory"
    },
    {
        "name": "Lakshadweep",
        "latitude": 10.5667,
        "longitude": 72.6417,
        "famous_for": "Coral Reefs and Beaches",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/An_Uninhabited_Island_in_Lakshadweep.JPG/320px-An_Uninhabited_Island_in_Lakshadweep.JPG",
        "type": "union_territory"
    },
    {
        "name": "Puducherry",
        "latitude": 11.9416,
        "longitude": 79.8083,
        "famous_for": "French Colonial Architecture and Auroville",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Puducherry_beach.jpg/320px-Puducherry_beach.jpg",
        "type": "union_territory"
    }
]

# https://api.spoonacular.com/recipes/complexSearch?query=pasta&apiKey=
res_1 = {
    "results": [
        {
            "id": 654959,
            "title": "Pasta With Tuna",
            "image": "https://spoonacular.com/recipeImages/654959-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 511728,
            "title": "Pasta Margherita",
            "image": "https://spoonacular.com/recipeImages/511728-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654857,
            "title": "Pasta On The Border",
            "image": "https://spoonacular.com/recipeImages/654857-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654883,
            "title": "Pasta Vegetable Soup",
            "image": "https://spoonacular.com/recipeImages/654883-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654928,
            "title": "Pasta With Italian Sausage",
            "image": "https://spoonacular.com/recipeImages/654928-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654926,
            "title": "Pasta With Gorgonzola Sauce",
            "image": "https://spoonacular.com/recipeImages/654926-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654944,
            "title": "Pasta With Salmon Cream Sauce",
            "image": "https://spoonacular.com/recipeImages/654944-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654905,
            "title": "Pasta With Chickpeas and Kale",
            "image": "https://spoonacular.com/recipeImages/654905-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654901,
            "title": "Pasta With Chicken and Broccoli",
            "image": "https://spoonacular.com/recipeImages/654901-312x231.jpg",
            "imageType": "jpg"
        },
        {
            "id": 654913,
            "title": "Pasta With Chicken and Mushrooms",
            "image": "https://spoonacular.com/recipeImages/654913-312x231.jpg",
            "imageType": "jpg"
        }
    ],
    "offset": 0,
    "number": 10,
    "totalResults": 261
}

# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey= 
res_2 = {
    "results": [
        {
            "id": 654959,
            "title": "Pasta With Tuna",
            "image": "https://spoonacular.com/recipeImages/654959-312x231.jpg",
            "imageType": "jpg",
            "nutrition": {
                "nutrients": [
                    {
                        "name": "Fat",
                        "amount": 10.3185,
                        "unit": "g"
                    }
                ]
            }
        },
        {
            "id": 654857,
            "title": "Pasta On The Border",
            "image": "https://spoonacular.com/recipeImages/654857-312x231.jpg",
            "imageType": "jpg",
            "nutrition": {
                "nutrients": [
                    {
                        "name": "Fat",
                        "amount": 19.8995,
                        "unit": "g"
                    }
                ]
            }
        }
    ],
    "offset": 0,
    "number": 2,
    "totalResults": 133
}

# get all ingedient based on recipe ID
# https://api.spoonacular.com/recipes/{recipe ID}/ingredientWidget.json
res_3 = {
    "ingredients": [
        {
            "amount": {
                "metric": {
                    "unit": "g",
                    "value": 222.0
                },
                "us": {
                    "unit": "cups",
                    "value": 1.5
                }
            },
            "image": "blueberries.jpg",
            "name": "blueberries"
        },
        {
            "amount": {
                "metric": {
                    "unit": "",
                    "value": 1.0
                },
                "us": {
                    "unit": "",
                    "value": 1.0
                }
            },
            "image": "egg-white.jpg",
            "name": "egg white"
        },
        {
            "amount": {
                "metric": {
                    "unit": "Tbsps",
                    "value": 2.0
                },
                "us": {
                    "unit": "Tbsps",
                    "value": 2.0
                }
            },
            "image": "flour.png",
            "name": "flour"
        },
        {
            "amount": {
                "metric": {
                    "unit": "g",
                    "value": 150.0
                },
                "us": {
                    "unit": "cup",
                    "value": 0.75
                }
            },
            "image": "sugar-in-bowl.png",
            "name": "granulated sugar"
        },
        {
            "amount": {
                "metric": {
                    "unit": "tsp",
                    "value": 1.0
                },
                "us": {
                    "unit": "tsp",
                    "value": 1.0
                }
            },
            "image": "lemon-juice.jpg",
            "name": "fresh lemon juice"
        },
        {
            "amount": {
                "metric": {
                    "unit": "pinch",
                    "value": 1.0
                },
                "us": {
                    "unit": "pinch",
                    "value": 1.0
                }
            },
            "image": "ground-nutmeg.jpg",
            "name": "nutmeg"
        },
        {
            "amount": {
                "metric": {
                    "unit": "",
                    "value": 2.0
                },
                "us": {
                    "unit": "",
                    "value": 2.0
                }
            },
            "image": "pie-crust.jpg",
            "name": "pie dough round"
        },
        {
            "amount": {
                "metric": {
                    "unit": "Tbsps",
                    "value": 2.0
                },
                "us": {
                    "unit": "Tbsps",
                    "value": 2.0
                }
            },
            "image": "tapioca-pearls.png",
            "name": "quick cooking tapioca"
        },
        {
            "amount": {
                "metric": {
                    "unit": "g",
                    "value": 305.0
                },
                "us": {
                    "unit": "cups",
                    "value": 2.5
                }
            },
            "image": "rhubarb.jpg",
            "name": "trimmed rhubarb"
        },
        {
            "amount": {
                "metric": {
                    "unit": "tsps",
                    "value": 0.333
                },
                "us": {
                    "unit": "tsps",
                    "value": 0.333
                }
            },
            "image": "salt.jpg",
            "name": "salt"
        },
        {
            "amount": {
                "metric": {
                    "unit": "Tbsps",
                    "value": 0.5
                },
                "us": {
                    "unit": "Tbsps",
                    "value": 0.5
                }
            },
            "image": "butter-sliced.jpg",
            "name": "unsalted butter"
        }
    ]
}

# get all instruction based on recipe ID
# https://api.spoonacular.com/recipes/324694/analyzedInstructions
res_4 = [
    {
        "name": "",
        "steps": [
            {
                "equipment": [
                    {
                        "id": 404784,
                        "image": "oven.jpg",
                        "name": "oven",
                        "temperature": {
                            "number": 200.0,
                            "unit": "Fahrenheit"
                        }
                    }
                ],
                "ingredients": [],
                "number": 1,
                "step": "Preheat the oven to 200 degrees F."
            },
            {
                "equipment": [
                    {
                        "id": 404661,
                        "image": "whisk.png",
                        "name": "whisk"
                    },
                    {
                        "id": 404783,
                        "image": "bowl.jpg",
                        "name": "bowl"
                    }
                ],
                "ingredients": [
                    {
                        "id": 19334,
                        "image": "light-brown-sugar.jpg",
                        "name": "light brown sugar"
                    },
                    {
                        "id": 19335,
                        "image": "sugar-in-bowl.png",
                        "name": "granulated sugar"
                    },
                    {
                        "id": 18371,
                        "image": "white-powder.jpg",
                        "name": "baking powder"
                    },
                    {
                        "id": 18372,
                        "image": "white-powder.jpg",
                        "name": "baking soda"
                    },
                    {
                        "id": 12142,
                        "image": "pecans.jpg",
                        "name": "pecans"
                    },
                    {
                        "id": 20081,
                        "image": "flour.png",
                        "name": "all purpose flour"
                    },
                    {
                        "id": 2047,
                        "image": "salt.jpg",
                        "name": "salt"
                    }
                ],
                "number": 2,
                "step": "Whisk together the flour, pecans, granulated sugar, light brown sugar, baking powder, baking soda, and salt in a medium bowl."
            },
            {
                "equipment": [
                    {
                        "id": 404661,
                        "image": "whisk.png",
                        "name": "whisk"
                    },
                    {
                        "id": 404783,
                        "image": "bowl.jpg",
                        "name": "bowl"
                    }
                ],
                "ingredients": [
                    {
                        "id": 2050,
                        "image": "vanilla-extract.jpg",
                        "name": "vanilla extract"
                    },
                    {
                        "id": 93622,
                        "image": "vanilla.jpg",
                        "name": "vanilla bean"
                    },
                    {
                        "id": 1230,
                        "image": "buttermilk.jpg",
                        "name": "buttermilk"
                    },
                    {
                        "id": 1123,
                        "image": "egg.png",
                        "name": "egg"
                    }
                ],
                "number": 3,
                "step": "Whisk together the eggs, buttermilk, butter and vanilla extract and vanilla bean in a small bowl."
            },
            {
                "equipment": [],
                "ingredients": [
                    {
                        "id": 1123,
                        "image": "egg.png",
                        "name": "egg"
                    }
                ],
                "number": 4,
                "step": "Add the egg mixture to the dry mixture and gently mix to combine. Do not overmix."
            },
            {
                "equipment": [],
                "ingredients": [],
                "length": {
                    "number": 15,
                    "unit": "minutes"
                },
                "number": 5,
                "step": "Let the batter sit at room temperature for at least 15 minutes and up to 30 minutes before using."
            },
            {
                "equipment": [
                    {
                        "id": 404779,
                        "image": "griddle.jpg",
                        "name": "griddle"
                    },
                    {
                        "id": 404645,
                        "image": "pan.png",
                        "name": "frying pan"
                    }
                ],
                "ingredients": [],
                "length": {
                    "number": 3,
                    "unit": "minutes"
                },
                "number": 6,
                "step": "Heat a cast iron or nonstick griddle pan over medium heat and brush with melted butter. Once the butter begins to sizzle, use 2 tablespoons of the batter for each pancake and cook until the bubbles appear on the surface and the bottom is golden brown, about 2 minutes, flip over and cook until the bottom is golden brown, 1 to 2 minutes longer."
            },
            {
                "equipment": [
                    {
                        "id": 404784,
                        "image": "oven.jpg",
                        "name": "oven",
                        "temperature": {
                            "number": 200.0,
                            "unit": "Fahrenheit"
                        }
                    }
                ],
                "ingredients": [],
                "number": 7,
                "step": "Transfer the pancakes to a platter and keep warm in a 200 degree F oven."
            },
            {
                "equipment": [],
                "ingredients": [
                    {
                        "id": 10014037,
                        "image": "bourbon.png",
                        "name": "bourbon"
                    }
                ],
                "number": 8,
                "step": "Serve 6 pancakes per person, top each with some of the bourbon butter."
            },
            {
                "equipment": [],
                "ingredients": [
                    {
                        "id": 19336,
                        "image": "powdered-sugar.jpg",
                        "name": "powdered sugar"
                    },
                    {
                        "id": 19911,
                        "image": "maple-syrup.png",
                        "name": "maple syrup"
                    }
                ],
                "number": 9,
                "step": "Drizzle with warm maple syrup and dust with confectioners' sugar."
            },
            {
                "equipment": [],
                "ingredients": [
                    {
                        "id": 12142,
                        "image": "pecans.jpg",
                        "name": "pecans"
                    }
                ],
                "number": 10,
                "step": "Garnish with fresh mint sprigs and more toasted pecans, if desired."
            }
        ]
    },
    {
        "name": "Bourbon Molasses Butter",
        "steps": [
            {
                "equipment": [
                    {
                        "id": 404669,
                        "image": "sauce-pan.jpg",
                        "name": "sauce pan"
                    }
                ],
                "ingredients": [
                    {
                        "id": 10014037,
                        "image": "bourbon.png",
                        "name": "bourbon"
                    },
                    {
                        "id": 19335,
                        "image": "sugar-in-bowl.png",
                        "name": "sugar"
                    }
                ],
                "number": 1,
                "step": "Combine the bourbon and sugar in a small saucepan and cook over high heat until reduced to 3 tablespoons, remove and let cool."
            },
            {
                "equipment": [
                    {
                        "id": 404771,
                        "image": "food-processor.png",
                        "name": "food processor"
                    }
                ],
                "ingredients": [
                    {
                        "id": 19304,
                        "image": "molasses.jpg",
                        "name": "molasses"
                    },
                    {
                        "id": 10014037,
                        "image": "bourbon.png",
                        "name": "bourbon"
                    },
                    {
                        "id": 2047,
                        "image": "salt.jpg",
                        "name": "salt"
                    }
                ],
                "number": 2,
                "step": "Put the butter, molasses, salt and cooled bourbon mixture in a food processor and process until smooth."
            },
            {
                "equipment": [
                    {
                        "id": 404730,
                        "image": "plastic-wrap.jpg",
                        "name": "plastic wrap"
                    },
                    {
                        "id": 404783,
                        "image": "bowl.jpg",
                        "name": "bowl"
                    }
                ],
                "ingredients": [],
                "number": 3,
                "step": "Scrape into a bowl, cover with plastic wrap and refrigerate for at least 1 hour to allow the flavors to meld."
            },
            {
                "equipment": [],
                "ingredients": [],
                "length": {
                    "number": 30,
                    "unit": "minutes"
                },
                "number": 4,
                "step": "Remove from the refrigerator about 30 minutes before using to soften."
            }
        ]
    }
]

# get all ingredient and instructions
# https://api.spoonacular.com/recipes/1003464/information?apiKey=
res_5 = {
    "vegetarian": True,
    "vegan": False,
    "glutenFree": False,
    "dairyFree": False,
    "veryHealthy": False,
    "cheap": False,
    "veryPopular": False,
    "sustainable": False,
    "lowFodmap": False,
    "weightWatcherSmartPoints": 11,
    "gaps": "no",
    "preparationMinutes": -1,
    "cookingMinutes": -1,
    "aggregateLikes": 0,
    "healthScore": 1,
    "creditsText": "nytimes.com",
    "sourceName": "nytimes.com",
    "pricePerServing": 104.08,
    "extendedIngredients": [
        {
            "id": 9050,
            "aisle": "Produce",
            "image": "blueberries.jpg",
            "consistency": "SOLID",
            "name": "blueberries",
            "nameClean": "blueberries",
            "original": "1 ½ cups/226 grams blueberries or blackberries",
            "originalName": "226 grams blueberries or blackberries",
            "amount": 1.5,
            "unit": "cups",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 1.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 222.0,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 1124,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "egg-white.jpg",
            "consistency": "SOLID",
            "name": "egg white",
            "nameClean": "egg whites",
            "original": "1 egg white, whisked with 1 tablespoon water",
            "originalName": "egg white, whisked with 1 tablespoon water",
            "amount": 1.0,
            "unit": "",
            "meta": [
                "with 1 tablespoon water"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 20081,
            "aisle": "Baking",
            "image": "flour.png",
            "consistency": "SOLID",
            "name": "flour",
            "nameClean": "wheat flour",
            "original": "2 tablespoons all-purpose flour",
            "originalName": "all-purpose flour",
            "amount": 2.0,
            "unit": "tablespoons",
            "meta": [
                "all-purpose"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        },
        {
            "id": 19335,
            "aisle": "Baking",
            "image": "sugar-in-bowl.png",
            "consistency": "SOLID",
            "name": "granulated sugar",
            "nameClean": "sugar",
            "original": "¾ cup/150 grams granulated sugar, more for sprinkling",
            "originalName": "150 grams granulated sugar, more for sprinkling",
            "amount": 0.75,
            "unit": "cup",
            "meta": [
                "for sprinkling"
            ],
            "measures": {
                "us": {
                    "amount": 0.75,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 150.0,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 9152,
            "aisle": "Produce",
            "image": "lemon-juice.jpg",
            "consistency": "LIQUID",
            "name": "lemon juice",
            "nameClean": "lemon juice",
            "original": "1 teaspoon fresh lemon juice",
            "originalName": "fresh lemon juice",
            "amount": 1.0,
            "unit": "teaspoon",
            "meta": [
                "fresh"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "tsp",
                    "unitLong": "teaspoon"
                }
            }
        },
        {
            "id": 2025,
            "aisle": "Spices and Seasonings",
            "image": "ground-nutmeg.jpg",
            "consistency": "SOLID",
            "name": "nutmeg",
            "nameClean": "nutmeg",
            "original": "Pinch of freshly grated nutmeg",
            "originalName": "Pinch of freshly grated nutmeg",
            "amount": 1.0,
            "unit": "pinch",
            "meta": [
                "freshly grated"
            ],
            "measures": {
                "us": {
                    "amount": 1.0,
                    "unitShort": "pinch",
                    "unitLong": "pinch"
                },
                "metric": {
                    "amount": 1.0,
                    "unitShort": "pinch",
                    "unitLong": "pinch"
                }
            }
        },
        {
            "id": 18334,
            "aisle": "Refrigerated",
            "image": "pie-crust.jpg",
            "consistency": "SOLID",
            "name": "pie dough round",
            "nameClean": "refrigerated pie crust",
            "original": "2 pie dough, chilled",
            "originalName": "pie dough, chilled",
            "amount": 2.0,
            "unit": "",
            "meta": [
                "chilled"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "",
                    "unitLong": ""
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "",
                    "unitLong": ""
                }
            }
        },
        {
            "id": 93660,
            "aisle": "Baking",
            "image": "tapioca-pearls.png",
            "consistency": "SOLID",
            "name": "quick cooking tapioca",
            "nameClean": "quick cooking tapioca",
            "original": "2 tablespoons quick-cooking tapioca (also called instant, minute or small pearl tapioca)",
            "originalName": "quick-cooking tapioca (also called instant, minute or small pearl tapioca)",
            "amount": 2.0,
            "unit": "tablespoons",
            "meta": [
                "(also called instant, minute or small pearl tapioca)"
            ],
            "measures": {
                "us": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 2.0,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        },
        {
            "id": 9307,
            "aisle": "Produce",
            "image": "rhubarb.jpg",
            "consistency": "SOLID",
            "name": "rhubarb",
            "nameClean": "rhubarb",
            "original": "2 ½ cups/312 grams rhubarb, trimmed and cut into 1/2- to 1-inch lengths",
            "originalName": "312 grams rhubarb, trimmed and cut into 1/2- to 1-inch lengths",
            "amount": 2.5,
            "unit": "cups",
            "meta": [
                "trimmed",
                "cut into 1/2- to 1-inch lengths"
            ],
            "measures": {
                "us": {
                    "amount": 2.5,
                    "unitShort": "cups",
                    "unitLong": "cups"
                },
                "metric": {
                    "amount": 305.0,
                    "unitShort": "g",
                    "unitLong": "grams"
                }
            }
        },
        {
            "id": 2047,
            "aisle": "Spices and Seasonings",
            "image": "salt.jpg",
            "consistency": "SOLID",
            "name": "salt",
            "nameClean": "table salt",
            "original": "1/3 teaspoon salt",
            "originalName": "salt",
            "amount": 0.33333334,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
                "us": {
                    "amount": 0.333,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                },
                "metric": {
                    "amount": 0.333,
                    "unitShort": "tsps",
                    "unitLong": "teaspoons"
                }
            }
        },
        {
            "id": 1145,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "butter-sliced.jpg",
            "consistency": "SOLID",
            "name": "unsalted butter",
            "nameClean": "unsalted butter",
            "original": "½ tablespoon cold unsalted butter",
            "originalName": "cold unsalted butter",
            "amount": 0.5,
            "unit": "tablespoon",
            "meta": [
                "unsalted",
                "cold"
            ],
            "measures": {
                "us": {
                    "amount": 0.5,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                },
                "metric": {
                    "amount": 0.5,
                    "unitShort": "Tbsps",
                    "unitLong": "Tbsps"
                }
            }
        }
    ],
    "id": 1003464,
    "title": "Blueberry Rhubarb Pie",
    "readyInMinutes": 60,
    "servings": 8,
    "sourceUrl": "https://cooking.nytimes.com/recipes/1018681-blueberry-rhubarb-pie",
    "image": "https://spoonacular.com/recipeImages/1003464-556x370.jpg",
    "imageType": "jpg",
    "summary": "Blueberry Rhubarb Pie is a dessert that serves 8. Watching your figure? This lacto ovo vegetarian recipe has <b>317 calories</b>, <b>4g of protein</b>, and <b>12g of fat</b> per serving. For <b>$1.04 per serving</b>, this recipe <b>covers 6%</b> of your daily requirements of vitamins and minerals. 1 person has made this recipe and would make it again. Head to the store and pick up salt, nutmeg, flour, and a few other things to make it today. It can be enjoyed any time, but it is especially good for <b>Mother's Day</b>. It is brought to you by cooking.nytimes.com. From preparation to the plate, this recipe takes around <b>1 hour</b>. With a spoonacular <b>score of 32%</b>, this dish is rather bad. Try <a href=\"https://spoonacular.com/recipes/blueberry-rhubarb-pie-510170\">Blueberry Rhubarb Pie</a>, <a href=\"https://spoonacular.com/recipes/blueberry-rhubarb-tarts-484435\">Blueberry-Rhubarb Tarts</a>, and <a href=\"https://spoonacular.com/recipes/blueberry-rhubarb-muffins-512542\">Blueberry Rhubarb Muffins</a> for similar recipes.",
    "cuisines": [],
    "dishTypes": [
        "side dish"
    ],
    "diets": [
        "lacto ovo vegetarian"
    ],
    "occasions": [
        "spring",
        "mother's day"
    ],
    "winePairing": {},
    "instructions": "<p>Heat oven to 425 degrees. Roll out both crusts. Line a deep 9-inch pie pan with the bottom crust and return both crusts to the refrigerator.</p><p>              In a medium bowl, combine rhubarb, berries, sugar, flour, tapioca, salt, nutmeg and lemon juice. Toss to coat and combine, then scoop into waiting bottom crust. The fruit should come up to within 1/2-inch of the rim of the pan; do not overfill. If necessary, add more or subtract some of the fruit. Break the butter into pieces and dot over the fruit.</p><p>              Lay top crust over filling. Trim excess dough from the edges and crimp, then cut 6 or 7 vents on top. Brush a light coating of egg wash over the crust, including the edges.</p><p>              Bake for 20 minutes. Reduce heat to 375 degrees. Bake another 25 minutes, then open the oven and quickly sprinkle the crust with a thin coating of granulated sugar. Bake another 10 to 15 minutes, or until you see steady bubbling in the filling coming through the vents.</p><p>              Remove pie from oven and listen to it: if the crust is sizzling, and the filling is audibly bubbling against the top crust, it is done. Let cool completely before serving.</p>",
    "analyzedInstructions": [
        {
            "name": "",
            "steps": [
                {
                    "number": 1,
                    "step": "Heat oven to 425 degrees.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ]
                },
                {
                    "number": 2,
                    "step": "Roll out both crusts. Line a deep 9-inch pie pan with the bottom crust and return both crusts to the refrigerator.",
                    "ingredients": [
                        {
                            "id": 0,
                            "name": "crust",
                            "localizedName": "crust",
                            "image": ""
                        },
                        {
                            "id": 0,
                            "name": "roll",
                            "localizedName": "roll",
                            "image": "dinner-yeast-rolls.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 405915,
                            "name": "pie form",
                            "localizedName": "pie form",
                            "image": "pie-pan.png"
                        }
                    ]
                },
                {
                    "number": 3,
                    "step": "In a medium bowl, combine rhubarb, berries, sugar, flour, tapioca, salt, nutmeg and lemon juice. Toss to coat and combine, then scoop into waiting bottom crust. The fruit should come up to within 1/2-inch of the rim of the pan; do not overfill. If necessary, add more or subtract some of the fruit. Break the butter into pieces and dot over the fruit.",
                    "ingredients": [
                        {
                            "id": 9152,
                            "name": "lemon juice",
                            "localizedName": "lemon juice",
                            "image": "lemon-juice.jpg"
                        },
                        {
                            "id": 1009054,
                            "name": "berries",
                            "localizedName": "berries",
                            "image": "berries-mixed.jpg"
                        },
                        {
                            "id": 9307,
                            "name": "rhubarb",
                            "localizedName": "rhubarb",
                            "image": "rhubarb.jpg"
                        },
                        {
                            "id": 20068,
                            "name": "tapioca",
                            "localizedName": "tapioca",
                            "image": "sago-pearls.png"
                        },
                        {
                            "id": 1001,
                            "name": "butter",
                            "localizedName": "butter",
                            "image": "butter-sliced.jpg"
                        },
                        {
                            "id": 2025,
                            "name": "nutmeg",
                            "localizedName": "nutmeg",
                            "image": "ground-nutmeg.jpg"
                        },
                        {
                            "id": 0,
                            "name": "crust",
                            "localizedName": "crust",
                            "image": ""
                        },
                        {
                            "id": 20081,
                            "name": "all purpose flour",
                            "localizedName": "all purpose flour",
                            "image": "flour.png"
                        },
                        {
                            "id": 9431,
                            "name": "fruit",
                            "localizedName": "fruit",
                            "image": "mixed-fresh-fruit.jpg"
                        },
                        {
                            "id": 19335,
                            "name": "sugar",
                            "localizedName": "sugar",
                            "image": "sugar-in-bowl.png"
                        },
                        {
                            "id": 2047,
                            "name": "salt",
                            "localizedName": "salt",
                            "image": "salt.jpg"
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404783,
                            "name": "bowl",
                            "localizedName": "bowl",
                            "image": "bowl.jpg"
                        },
                        {
                            "id": 404645,
                            "name": "frying pan",
                            "localizedName": "frying pan",
                            "image": "pan.png"
                        }
                    ]
                },
                {
                    "number": 4,
                    "step": "Lay top crust over filling. Trim excess dough from the edges and crimp, then cut 6 or 7 vents on top.",
                    "ingredients": [
                        {
                            "id": 0,
                            "name": "crust",
                            "localizedName": "crust",
                            "image": ""
                        },
                        {
                            "id": 0,
                            "name": "dough",
                            "localizedName": "dough",
                            "image": "pizza-dough"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 5,
                    "step": "Brush a light coating of egg wash over the crust, including the edges.",
                    "ingredients": [
                        {
                            "id": 0,
                            "name": "crust",
                            "localizedName": "crust",
                            "image": ""
                        },
                        {
                            "id": 1123,
                            "name": "egg",
                            "localizedName": "egg",
                            "image": "egg.png"
                        }
                    ],
                    "equipment": []
                },
                {
                    "number": 6,
                    "step": "Bake for 20 minutes. Reduce heat to 375 degrees.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ],
                    "length": {
                        "number": 20,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 7,
                    "step": "Bake another 25 minutes, then open the oven and quickly sprinkle the crust with a thin coating of granulated sugar.",
                    "ingredients": [
                        {
                            "id": 10719335,
                            "name": "granulated sugar",
                            "localizedName": "granulated sugar",
                            "image": "sugar-in-bowl.png"
                        },
                        {
                            "id": 0,
                            "name": "crust",
                            "localizedName": "crust",
                            "image": ""
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ],
                    "length": {
                        "number": 25,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 8,
                    "step": "Bake another 10 to 15 minutes, or until you see steady bubbling in the filling coming through the vents.",
                    "ingredients": [],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ],
                    "length": {
                        "number": 10,
                        "unit": "minutes"
                    }
                },
                {
                    "number": 9,
                    "step": "Remove pie from oven and listen to it: if the crust is sizzling, and the filling is audibly bubbling against the top crust, it is done.",
                    "ingredients": [
                        {
                            "id": 0,
                            "name": "crust",
                            "localizedName": "crust",
                            "image": ""
                        }
                    ],
                    "equipment": [
                        {
                            "id": 404784,
                            "name": "oven",
                            "localizedName": "oven",
                            "image": "oven.jpg"
                        }
                    ]
                },
                {
                    "number": 10,
                    "step": "Let cool completely before serving.",
                    "ingredients": [],
                    "equipment": []
                }
            ]
        }
    ],
    "originalId": None,
    "spoonacularScore": 27.726211547851562
}
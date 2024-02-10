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
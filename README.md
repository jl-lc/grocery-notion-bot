# grocery-notion-bot
Python bot for automating purchasing groceries with tracking in Notion (in progress)
# Motivation
Notion have been a great all-in-one tool for a lot of things that I keep track of, namely task management, meal planning, and project progress tracking are a couple that I use often in my workspace. Recently, I have found myself using Notion less because of the increased workload at school which throws off the task management and meal planning system that I have developed. This project is to make the process of meal prepping as seamless as possible so that it is more enjoyable and effortless even compared to eating out.
# Idea
The design philosophy for this is to reduce the number of actions that I need to do and make the things I have to do manually as effortless as possible to minimize friction in meal prepping. The intention with this project is every Friday, I can make a choice of what food to meal prep for the next week and have this script query from the database of recipes that I have made in Notion, check for which ingredients need to be purchased, and automatically selects the items on Instacart with Selenium and bring me to the purchase confirmation page.

Once I have cooked for the week with the purchased ingredients, the idea is to update the database so that the script can update the stock for each ingredient. To update the database that I have cooked my meal, the plan is to scan my phone on a NFC tag that will trigger a script in my phone to update on Notion.

The NFC tag idea will extend beyond the scope of this project that will act like a checkpoint for every task that I have to do, starting with meal prep completion. Like checkpoints in a game, or similar to closing activity rings on an Apple Watch, the theory is that this NFC tag checkpoint as an arbitrary goal will eventually turn into a (maybe?) healthy obsession with the dopamine hits of each task completion.
# Current Version
- Completed the basis of querying pages
# Action Items
- Full redesign of the recipe database for better integration with Python
- Complete page query for stock and price of ingredients list of each dish
- Develop page update function
# Resources
[Notion API Reference](https://developers.notion.com/reference/intro)

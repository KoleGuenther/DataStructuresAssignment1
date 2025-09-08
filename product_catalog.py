from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
for product in products:
    product['tags'] = set(product['tags'])


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommend_products=[]
    for product in products:
        matches = count_matches(product['tags'], customer_tags)
        recommend_products.append({'name': product['name'], 'matches': matches})
    recommend_products.sort(key=lambda x: x['matches'], reverse=True)
    return recommend_products



# TODO: Step 7 - Call your function and print the results

results = recommend_products(products, customer_preferences)

print("Recommended Products:")
for result in results:
    print(f"{result['name']}: {result['matches']} matches")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# I used loops to iterate over the lists/sets of the products and matches, as well as the tags. This was to speed up the process of finding matches by using sets, since lists are less efficient than sets :( . I used set intersections to find common tags between products and customer preferences to find all the products that the customer might like, then sorted them by the most amount of matches so the products at the top were the most likely to be correctly recommended. If loops were not used, it would take WAY too much time to code everything by hand, individually checking everything manually.
# 2. How might this code change if you had 1000+ products?
# I believe the same code would still work, but it would take longer to run. To optimize it, I might want to use other data structures to speed up the search process, but the set intersections are still very efficient, although the loops would take longer than they do now. With many many products, I would want to overall optimize the code to run as fast as possible since there will be so many connections that can be made with products, and loops would take near forever to run with the current code.

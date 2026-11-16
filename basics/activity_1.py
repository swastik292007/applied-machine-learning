import numpy as np
prices=np.array([29.99,49.99,19.99])
quantities=np.array([1,2,3])

revenue=prices*quantities
print("revenue for each product",revenue)
print("total revenue",np.sum(revenue))

#mean price
mean_price=np.mean(prices)
print("mean price",mean_price)

#standard deviation of prices
std_price=np.std(prices)    
print("standard deviation of prices",std_price)

#expensive itmes 
expensive_items=prices[prices>40]
print("expensive items",expensive_items)

sales=np.array([100,200,300,400,500,600,700,800,900,1000,1100,1200]) 

sales_matrix=sales.reshape(4,3)
print("sales matrix")
print(sales_matrix)
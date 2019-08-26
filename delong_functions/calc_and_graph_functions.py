import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import pandas as pd

plt.style.use('seaborn-whitegrid')
matplotlib.rc("font", family="Verdana")
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 6
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size

plt.close('all')





def draw_demand_line(maximum_willingness_to_pay, demand_slope):
    """Draw a linear demand curve when provided with paratmeters in 
    slope-intercept form.
    
    Parameters
    ==========
    
    maximum_willingness_to_pay : float
        the y-axis (price axis) intercept of the demand curve; the
        highest willingness-to-pay for a unit of the commodity found
        in the marketplace
        
    demand_slope: float
        how many extra units must be purchased to lower the outstanding
        highest unsatisfied willingness-to-pay by one dollar; the slope of the 
        demand curve
        
    Returns
    =======
    
    None
    """
    
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = maximum_willingness_to_pay - demand_slope * x_vals
    plt.plot(x_vals, y_vals, color = "blue", label = "Demand")





def draw_supply_line(minimum_opportunity_cost, supply_slope):
    """Draw a supply demand curve when provided with paratmeters in 
    slope-intercept form.
    
    Parameters
    ==========
    
    minimum_opportunity_cost : float
        the y-axis (price axis) intercept of the supply curve; the
        lowest price at which the first producer finds it profitable
        to produce and sell a unit of the commodity in the marketplace;
        the minimum opportunity cost found among producers
        
    supply: float
        how many extra units must be purchased to raise the outstanding
        lowest remaining opportunity cost by one dollar; the slope of the 
        supply curve
        
    Returns
    =======
    
    None
    """
    
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = minimum_opportunity_cost + supply_slope * x_vals
    plt.plot(x_vals, y_vals, color = "green", label = "Supply")





def print_market_summary(consumer_surplus, producer_surplus, equilibrium_price, 
    equilibrium_quantity, market_for_title):
    """Function to print the crude table of the four market summary equilibrium
    summary statistics
    
    Parameters
    ==========
    
    consumer_surplus : float 
        the difference between the sum of satisfied willingnesses-to-pay by
        purchasers and the sum of prices they paid to suppliers; the maximum
        amount that could ever be extracted from purchasers by a threat to close
        the market down; calculated in standard_supply_and_demand_graph() and passed
        to print_market_summary()
    
    producer_surplus: float 
        the difference between the sum of revenue earned by suppliers and the
        sum of incurred opportunity costs by suppliers; the maximum amount that 
        could ever be extracted from suppliers by a threat to close the market 
        down; calculated in standard_supply_and_demand_graph() and passed to 
        print_market_summary()
    
    equilibrium_price: float
        the market price at which quantity supplied is equal to quantity 
        demanded; calculated in standard_supply_and_demand_graph() and passed
        to print_market_summary()
    
    equilibrium_quantity: float
        the quantity produced and sold at which quantity supplied is equal to
        quantity demanded; calculated in standard_supply_and_demand_graph() and passed
        to print_market_summary()
    
    market_for_title : string
        the market and commodity of the supply-and-demand equilibrium— for
        example: "Lattes at Euphoric State"; passed to standard_supply_and_demand_graph() 
        and then passed to print_market_summary()
        
    Returns
    =======
    
    None
    """
    print("")
    print("")
    print("SUMMARY: MARKET FOR " + market_for_title.upper())
    print("")
    print(round(consumer_surplus, 3), "= consumer surplus")
    print(round(producer_surplus, 3), "= producer surplus")
    print(round(equilibrium_price, 3), "= equilibrium price")
    print(round(equilibrium_quantity, 3), "= equilibrium quantity")
    print("")
    print("")





def standard_supply_and_demand_graph(maximum_willingness_to_pay, demand_slope, 
    minimum_opportunity_cost, supply_slope, market_for_title):
    """
    Function to calculate a graph and summary market statistics from slope-intercept
    linear descriptions of supply and demand. Requires four floats for **maximum 
    willingness to pay** on the part of potential demanders, **minimum opportunity 
    cost** on the part of potential suppliers, demand and supply slopes, and a string
    identifying the market and commodity. Returns a matplotlib figure object, an ax
    subplots object, and a dictionary of market equilibrium summary statistics
    
    Parameters
    ==========
    
    consumer_surplus : float 
        the difference between the sum of satisfied willingnesses-to-pay by
        purchasers and the sum of prices they paid to suppliers; the maximum
        amount that could ever be extracted from purchasers by a threat to close
        the market down; calculated in standard_supply_and_demand_graph() and passed
        to print_market_summary()
    
    producer_surplus: float 
        the difference between the sum of revenue earned by suppliers and the
        sum of incurred opportunity costs by suppliers; the maximum amount that 
        could ever be extracted from suppliers by a threat to close the market 
        down; calculated in standard_supply_and_demand_graph() and passed to 
        print_market_summary()
    
    equilibrium_price: float
        the market price at which quantity supplied is equal to quantity 
        demanded; calculated in standard_supply_and_demand_graph() and passed
        to print_market_summary()
    
    equilibrium_quantity: float
        the quantity produced and sold at which quantity supplied is equal to
        quantity demanded; calculated in standard_supply_and_demand_graph() and passed
        to print_market_summary()
    
    market_for_title : string
        the market and commodity of the supply-and-demand equilibrium— for
        example: "Lattes at Euphoric State"; passed to standard_supply_and_demand_graph() 
        and then passed to print_market_summary()
        
    Returns
    =======
    
    fig, ax, eqiilibrium
    
    fig : matplotlib.figure.Figure
        the graph drawn by the function: the standard supply-and-demand graph with
        title, labels, legend, and annotated equilibrium point
        
    ax : matplotlib.axes._subplots.AxesSubplot
    
    equilibrium : dict
        A Python dictionary containing a string identifying the commodity market for
        which equilibrium has been calculated, and floats for thefour key market summary 
        statistics calculated in order to draw the supply-and-demand graph; all
        for further reference. The keys to the dictionary are all strings:
        
            "Equilibrium Price"—the market price at which quantity supplied is equal 
            to quantity demanded; calculated in standard_supply_and_demand_graph()
            
            "Equilibrium Quantity"—the quantity produced and sold at which quantity 
            supplied is equal to quantity demanded; calculated in 
            standard_supply_and_demand_graph()
            
            "Consumer Surplus"—the difference between the sum of satisfied 
            willingnesses-to-pay by purchasers and the sum of prices they paid 
            to suppliers; the maximum amount that could ever be extracted from 
            purchasers by a threat to close the market down; calculated in 
            standard_supply_and_demand_graph()
            
            "Producer Surplus"—the difference between the sum of revenue earned 
            by suppliers and the sum of incurred opportunity costs by suppliers; 
            the maximum amount that could ever be extracted from suppliers by any
            threat to close the market down; calculated in 
            standard_supply_and_demand_graph(): producer_surplus,
        
            "Market"—the market and commodity of the supply-and-demand equilibrium—
            for example: "Lattes at Euphoric State"; passed to 
            standard_supply_and_demand_graph()
    """
    
    equilibrium_quantity = ((maximum_willingness_to_pay - minimum_opportunity_cost)/
        (supply_slope + demand_slope))
    equilibrium_price = (maximum_willingness_to_pay - equilibrium_quantity * demand_slope)
    consumer_surplus = ((maximum_willingness_to_pay - equilibrium_price) * 
        equilibrium_quantity/2)
    producer_surplus = ((equilibrium_price - minimum_opportunity_cost) * 
        equilibrium_quantity/2)
    
    fig, ax = plt.subplots()
    max_x_lim = 1.5 * equilibrium_quantity
    max_y_lim = 1.2 * maximum_willingness_to_pay
    fig.suptitle("Supply and Demand Graph: \n" + market_for_title, size = "20")
    ax.set_xlim(0, max_x_lim)
    ax.set_ylim(0, max_y_lim)
    
    plt.plot(equilibrium_quantity, equilibrium_price, marker='o', 
        markersize=8, color="red")
    plt.text(equilibrium_quantity, 1.1 * equilibrium_price, 
        "Market Equilibrium: \n" + "Quantity = " + 
        str(round(equilibrium_quantity, 2)) + "\nPrice = " + 
        str(round(equilibrium_price, 2)), size = "8")
    plt.xlabel("Number of " + market_for_title, size = "10")
    plt.ylabel("Price/Value of " + market_for_title, size = "10")
    draw_demand_line(maximum_willingness_to_pay, demand_slope)
    draw_supply_line(minimum_opportunity_cost, supply_slope)
    plt.legend()
    fig.canvas.draw()
    
    equilibrium = {"Equilibrium Price": equilibrium_price,
        "Equilibrium Quantity": equilibrium_quantity,
        "Consumer Surplus": consumer_surplus,
        "Producer Surplus": producer_surplus,
        "Market": market_for_title}
    
    print_market_summary(consumer_surplus, producer_surplus, equilibrium_price, 
    equilibrium_quantity, market_for_title)

    return fig, ax, equilibrium






# ----
#
# These are calculation and graphics functions for Brad DeLong's jupyter notebooks. 
# Should exist in two copies, one each inside the delong_functions directories 
# of Brad DeLong's private jupyter notebook backup github repository and of 
# Brad DeLong's public eblog-support github repository.
#
# Use: from delong_functions.calc_and_graph_functions import *
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

def return_figures():

    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the five plotly visualizations

    """
    # Reading data from Sqlite database
    engine = create_engine('sqlite:///data/WB.db')
    print("test")
    df_land = pd.read_sql_table('Arable_Land', engine)

    color_discrete_map = {'United States':"#9e0142", 'China': "#d53e4f", 'Japan':"#f46d43", 'Germany':"#fdae61", 'United Kingdom':"#68551f", \
    'India':"#899c26", 'France':"#abdda4", 'Brazil':"#66c2a5", 'Italy': "#3288bd", 'Canada':"#5e4fa2"}
    countries = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']

    # first chart plots arable land from 1990 to 2015 in top 10 economies as a line chart
   
    fig1 = px.line(df_land, x = "Year",y = "Hectares_Person", color = "Country", color_discrete_map=color_discrete_map,
          markers = True, title = "Arable Land(Hectares) per Person in 2020", category_orders={"Country":countries})
    fig1.update_layout(title = {"x": 0.45, "y": 0.9}, title_font_size = 19)
    fig1.update_traces(marker = {"size":5, "symbol":4})
    
    # second chart plots ararble land for 2020 as a bar chart 
    df_2020 = df_land[df_land['Year'] == 2020]  
    fig2 = px.bar(df_2020, x = "Country", y = "Hectares_Person", 
            title = 'Arable Land(Hectares) per Person in 2020')
    fig2.update_layout(title = {"x": 0.5, "y": 0.9}, title_font_size = 19)


    # third chart plots percent of population that is rural from 1990 to 2015
    df_rural_pop_pct = pd.read_sql_table('Rural_Pop_Pct', engine)
   

    fig3 = px.line(df_rural_pop_pct, x = "Year", y= "Rural Population_Percent", color = "Country", markers = True,
          title= "Percentage of Rural Population Over Time", category_orders={"Country":countries},
          color_discrete_map=color_discrete_map)
    fig3.update_layout(title = {"x": 0.45, "y": 0.9}, title_font_size = 19)
    
    # fourth chart shows rural population vs arable land
    df_pop_forest = pd.read_sql_table('Rural_Pop_Forest_Area', engine)

    fig4 = px.scatter(df_pop_forest, x = "Rural Population", y = "Forest area(sq.km)", color = "Country",
    color_discrete_map=color_discrete_map, category_orders={"Country":countries},
    title = "Rural Population versus <br> Forested Area (Square Km) 1990-2020")
    fig4.update_layout(title = {"x": 0.45, "y": 0.9}, title_font_size = 19)
    fig4.update_traces(marker = {"size":5, "symbol":3})
  
        
    # five chart shows population in 2020
    df_2020 = df_pop_forest[df_pop_forest['Year']==2020]
   
    fig5 = px.bar(df_2020, x = "Country", y = "Rural Population", title = "Rural Population in 2020")
    fig5.update_layout(title = {"x": 0.5, "y": 0.9}, title_font_size = 19)
      
      # append all charts to the figures list
    figures = [fig1, fig2, fig3, fig4, fig5]
  
    return figures
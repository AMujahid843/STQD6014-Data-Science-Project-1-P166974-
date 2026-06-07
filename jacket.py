#!/usr/bin/env python
# coding: utf-8

# Jacket Module for STQD6014 Data Science Project 1 (P166974)

# PART 3 FUNCTIONS AND CLASSES

# 2.

# In[83]:


class Jacket():
    """A simple attempt to represent a jacket."""
    def __init__(self, manufacturer, size, colour, year):
        """Initialize attributes to describe a jacket."""
        self.manufacturer = manufacturer
        self.size = size
        self.colour = colour
        self.year = year
        self.hipsize = 97
        
    def info(self):
        """Short description about the jacket."""
        jacket_description = "Manufacturer: " + self.manufacturer + ", Size:" + self.size.upper() + ", Colour:" + self.colour + ", Year:" + str(self.year)
        return jacket_description.upper()
        
    def get_descriptive_name(self):
        """Print a statement about the jacket description."""
        print(self.size.upper() + "-sized " + self.colour + " jacket made in " + self.manufacturer.title() + " in " + str(self.year))

    def hip_size(self):
        """Print a statement about hip size of the jacket."""
        print("The jacket has hip size of " + str(self.hipsize) + " cm.")

    def update_hip_size(self, circumference):
        """Set the hip size of the jacket to the given value."""
        self.hipsize = circumference


# In[84]:


class LeatherJacket(Jacket):
    """Represent type of a jacket, specific to leather jackets."""
    def __init__(self, manufacturer, size, colour, year, leather_type):
        """Initialize attributes of the parent class (Jacket). Then initialize attributes specific to a leather jacket."""
        super().__init__(manufacturer, size, colour, year)
        self.leather_type = leather_type

    def describe_type(self):
        """Print a statement describing the type of the leather jacket."""
        print("This jacket is made of " + self.leather_type + ".")


# In[85]:


class PufferJacket(Jacket):
    """Represent type of a jacket, specific to puffer jackets."""
    def __init__(self, manufacturer, size, colour, year, puffer_style):
        """Initialize attributes of the parent class (Jacket). Then initialize attributes specific to a puffer jacket."""
        super().__init__(manufacturer, size, colour, year)
        self.puffer_style = puffer_style

    def describe_style(self):
        """Print a statement describing the style of the puffer jacket."""
        print("The style of this jacket is " + self.puffer_style + ".")


# In[ ]:





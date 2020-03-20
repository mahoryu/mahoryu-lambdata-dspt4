import pandas as pd


# OOP approach with inheritance

class CustomFrame(pd.DataFrame):
    """
    A custom frame that builds off the pandas data frame, adding a new method.
    """

    def add_state_names(self):
        """
        Adds corresponding state names to a data frame
        :param X: the dataframe
        :param state_column: (string) the column name with the state abbreviations.
        :return: a new df with the new column
        """

        # a map used for the conversion
        names_map = {
            "AL": "Alabama",
            "AK": "Alaska",
            "AZ": "Arizona",
            "AR": "Arkansas",
            "CA": "California",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DE": "Delaware",
            "FL": "Florida",
            "GA": "Georgia",
            "HI": "Hawaii",
            "ID": "Idaho",
            "IL": "Illinois",
            "IN": "Indiana",
            "IA": "Iowa",
            "KS": "Kansas",
            "KY": "Kentucky",
            "LA": "Louisiana",
            "ME": "Maine",
            "MD": "Maryland",
            "MA": "Massachusetts",
            "MI": "Michigan",
            "MN": "Minnesota",
            "MS": "Mississippi",
            "MO": "Missouri",
            "MT": "Montana",
            "NE": "Nebraska",
            "NV": "Nevada",
            "NH": "New Hampshire",
            "NJ": "New Jersey",
            "NM": "New Mexico",
            "NY": "New York",
            "NC": "North Carolina",
            "ND": "North Dakota",
            "OH": "Ohio",
            "OK": "Oklahoma",
            "OR": "Oregon",
            "PA": "Pennsylvania",
            "RI": "Rhode Island",
            "SC": "South Carolina",
            "SD": "South Dakota",
            "TN": "Tennessee",
            "TX": "Texas",
            "UT": "Utah",
            "VT": "Vermont",
            "VA": "Virginia",
            "WA": "Washington",
            "WV": "West Virginia",
            "WI": "Wisconsin",
            "WY": "Wyoming",
            "DC": "District of Columbia"
        }
        self["State_Names"] = self["abbrev"].map(names_map)


if __name__ == "__main__":

    df1 = pd.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(custom_df.head())
    custom_df.add_state_names()
    print(custom_df.head())

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from nltk.corpus import stopwords
import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import bert.params as pm

def industry_map():
    map = pd.read_csv("/Users/camerongallinger/code/cgallin/cover_genie/raw_data/job_postings_data/mappings/industries.csv")
    industry_map = {
    "Technology": [
        "Defense and Space Manufacturing", "Computer Hardware Manufacturing",
        "Software Development", "Computer Networking Products",
        "Technology, Information and Internet",
        "Telecommunications", "IT Services and IT Consulting",
        "Internet Marketplace Platforms", "Blockchain Services",
        "Desktop Computing Software Products", "IT System Custom Software Development",
        "Data Infrastructure and Analytics", "Social Networking Platforms",
        "Business Intelligence Platforms", "Digital Accessibility Services",
        "Internet News", "Internet Publishing","Technology and Software","Technology, Information and Media",
        "Information Technology and Services", "Computer Software", "Computer Networking","Computer and Network Security",
        "IT System Data Services","IT System Data Services","IT System Testing and Evaluation",
        "Information Services","Computer Games","Computer Hardware","Computer Networking Products",

    ],
    "Manufacturing": [
        "Consumer Electronics", "Medical Equipment Manufacturing",
        "Apparel Manufacturing", "Footwear Manufacturing",
        "Textile Manufacturing", "Furniture and Home Furnishings Manufacturing",
        "Beverage Manufacturing", "Pharmaceutical Manufacturing",
        "Sporting Goods Manufacturing", "Tobacco Manufacturing",
        "Plastics and Rubber Product Manufacturing", "Packaging and Containers Manufacturing",
        "Glass, Ceramics and Concrete Manufacturing", "Metal Valve, Ball, and Roller Manufacturing",
        "Robot Manufacturing", "Industrial Automation",
        "Transportation Equipment Manufacturing", "Oil and Gas",
        "Shipbuilding", "Chemical Manufacturing", "Mining",
        "Agricultural Chemical Manufacturing", "Paint, Coating, and Adhesive Manufacturing",
        "Electric Lighting Equipment Manufacturing", "Meat Products Manufacturing",
        "Wood Product Manufacturing", "Food and Beverage Manufacturing",
        "Machinery Manufacturing", "Construction Hardware Manufacturing",
        "Primary Metal Manufacturing", "Fabricated Metal Products",
        "HVAC and Refrigeration Equipment Manufacturing",
        "Engines and Power Transmission Equipment Manufacturing","Motor Vehicle Manufacturing",
        "Aerospace and Defense Manufacturing", "Electrical Equipment Manufacturing",
        "Aviation and Aerospace Component Manufacturing","Information Technology & Services",
        "Agriculture, Construction, Mining Machinery Manufacturing","Motor Vehicle Parts Manufacturing",
        "Renewable Energy Equipment Manufacturing","Semiconductor Manufacturing",
        "Magnetic and Optical Media Manufacturing",
        "Communications Equipment Manufacturing", "Audio and Video Equipment Manufacturing",
        "Renewable Energy Semiconductor Manufacturing","Mattress and Blinds Manufacturing",
        "Household and Institutional Furniture Manufacturing","Abrasives and Nonmetallic Minerals Manufacturing",
        "Industrial Machinery Manufacturing","Appliances, Electrical, and Electronics Manufacturing",
        "Automation Machinery Manufacturing", "Computers and Electronics Manufacturing","Plastics Manufacturing",

    ],
    "Healthcare and Biotechnology": [
        "Medical Practices", "Hospitals and Health Care",
        "Biotechnology Research", "Mental Health Care",
        "Medical Device", "Veterinary Services", "Nursing Homes and Residential Care Facilities",
        "Animal Feed Manufacturing", "Physical, Occupational and Speech Therapists",
        "Alternative Medicine", "Personal Care Product Manufacturing",
        "Cosmetics", "Pharmaceutical Manufacturing", "Dentists",
        "Medical and Diagnostic Laboratories", "Home Health Care Services","Health and Human Services",
        "Healthcare Services and Hospitals","Biotechnology","Pharmaceuticals",
        "Medical Devices","Healthcare Information Technology","Public Health","Hospitals",

    ],
    "Legal and Consulting Services": [
        "Law Practice", "Legal Services", "Business Consulting and Services",
        "Government Relations Services", "Strategic Management Services",
        "Alternative Dispute Resolution", "Public Policy Offices",
        "Environmental Services", "Operations Consulting",
    ],
    "Finance, Banking, Insurance and Accounting": [
        "Banking", "Insurance", "Real Estate",
        "Investment Banking", "Investment Management", "Capital Markets",
        "Venture Capital and Private Equity Principals", "Mortgage Services",
        "Credit Intermediation", "Loan Brokers", "Pension Funds",
        "Funds and Trusts", "Trusts and Estates","Accounting","Financial Services",
    ],
    "Real Estate, Property Management, and Construction": [
         "Leasing Non-residential Real Estate","Custruction","Real Estate",
        "Property Management",
    ],
    "Consumer Goods and Retail": [
        "Retail Apparel and Fashion", "Retail Groceries", "Retail Luxury Goods and Jewelry",
        "Online and Mail Order Retail", "Retail Motor Vehicles", "Retail Office Supplies and Gifts",
        "Retail Recyclable Materials & Used Merchandise", "Food and Beverage Retail",
        "Sporting Goods Manufacturing", "Retail Musical Instruments",
        "Retail Books and Printed News", "Retail Florists", "Tobacco Manufacturing",
        "Wholesale Import and Export", "Wholesale Luxury Goods and Jewelry",
        "Wholesale Food and Beverage", "Wholesale Chemical and Allied Products",
        "Wholesale Raw Farm Products","Retail","Retail Health and Personal Care Products",
        "Retail Pharmacies"
    ],
    "Entertainment and Media": [
        "Entertainment Providers", "Movies, Videos, and Sound",
        "Broadcast Media Production and Distribution", "Performing Arts",
        "Gambling Facilities and Casinos", "Artists and Writers", "Online Audio and Video Media",
        "Museums, Historical Sites, and Zoos", "Spectator Sports",
        "Golf Courses and Country Clubs", "Amusement Parks and Arcades",
        "Animation and Post-production", "Media Production", "Online Media",
        "Writers and Editors", "Theater Companies","Performing Arts and Spectator Sports",
    ],
    "Transportation and Logistics": [
        "Freight and Package Transportation", "Truck Transportation",
        "Rail Transportation", "Airlines and Aviation", "Urban Transit Services",
        "Transportation/Trucking/Railroad", "Pipeline Transportation",
        "Warehousing and Storage", "Ground Passenger Transportation",'Transportation, Logistics, Supply Chain and Storage',

    ],
    "Education and Research": [
        "Primary and Secondary Education", "Higher Education",
        "Education Administration Programs", "Research Services",
        "Think Tanks", "Technical and Vocational Training",
        "Non-profit Organizations", "Philanthropic Fundraising Services","Education",
        "E-Learning Providers","Education Management"
    ],
    "Government and Public Administration": [
        "Government Administration", "Public Safety", "Legislative Offices",
        "International Affairs", "Military and International Affairs",
        "Administration of Justice", "Public Policy Offices",
        "Courts of Law", "Correctional Institutions", "Housing Programs","Armed Forces",
        "Law Enforcement","Public Administration","Public Safety","International Affairs",

    ],
    "Environmental and Renewable Energy": [
        "Environmental Services", "Horticulture", "Renewables & Environment",
        "Solar Electric Power Generation", "Climate Data and Analytics",
        "Wind Electric Power Generation", "Climate Technology Product Manufacturing",
        "Conservation Programs",
    ],
    "Construction and Real Estate Development": [
        "Building Construction", "Residential Building Construction",
        "Nonresidential Building Construction", "Utility System Construction",
        "Specialty Trade Contractors", "Architecture and Planning",
        "Surveying and Mapping Services", "Civil Engineering","Construction and Real Estate Development",
        "Wholesale Building Materials","Construction","Water, Waste, Steam, and Air Conditioning Services",
    ],
    "Hospitality, Travel, and Food Service" : [
        "Restaurants and Food Service", "Hospitality", "Food Production",
        "Food and Beverage Manufacturing", "Food and Beverage Retail","Restaurants",
        "Food Production", "Food & Beverages", "Travel Arrangements","Food and Beverage Services",
        "Bed-and-Breakfasts, Hostels, Homestays","Wineries", "Caterers","Events Services",

    ],
    "Ambiguous or Placeholder Entries": [
        "nan", "Programs", "Non-descriptive placeholders from the list"
    ]
    }
    # Create a reverse mapping from industry names to their corresponding keys
    reverse_industry_map = {industry: key for key, industries in industry_map.items() for industry in industries}
    # Replace the values in map.industry_name with their "corresponding keys
    map["sub_industry_name"]=map["industry_name"]
    map["industry_name"]=map['industry_name'].map(lambda x : reverse_industry_map[x] if x in reverse_industry_map.keys() else x)
    return map

def load_data():
    df = pd.read_csv("/Users/camerongallinger/code/cgallin/cover_genie/raw_data/job_postings_data/postings.csv")
    map = industry_map()
    industries = pd.read_csv("/Users/camerongallinger/code/cgallin/cover_genie/raw_data/job_postings_data/jobs/job_industries.csv")
    df = df.merge(industries.merge(map,how="left", on ="industry_id").set_index("industry_id"),how="left", on ="job_id")
    big_industries=['Healthcare and Biotechnology',
        'Technology',
        'Manufacturing',
        'Finance, Banking, Insurance and Accounting',
        'Consumer Goods and Retail',
        'Staffing and Recruiting',
        'Hospitality, Travel, and Food Service',
        'Education and Research',
        'Construction and Real Estate Development',
        'Legal and Consulting Services',
        'Transportation and Logistics']
    df = df[df['industry_name'].isin(big_industries)]
    df= df.dropna(subset=["description"])
    return df["description"], df["industry_name"]

def clean_text(text):

    sw = stopwords.words('english')
    jpsw = [
        "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "is",
        "it", "of", "on", "or", "that", "the", "this", "to", "with", "you", "your",
        "we", "us", "our", "will", "can", "may", "should", "must", "if", "but",
        "about", "above", "below", "over", "under", "after", "before", "while",
        "during", "within", "without", "between", "so", "such", "all", "any",
        "some", "more", "most", "each", "every", "either", "neither", "both",
        "few", "several", "many", "other", "another", "those", "these", "there",
        "here", "who", "whom", "whose", "which", "what", "where", "when", "how",
        "why", "into", "onto", "upon", "through", "via", "per", "including",
        "across", "based", "according", "looking", "responsible", "required",
        "desired", "preferred", "qualifications", "skills", "experience",
        "knowledge", "ability", "work", "role", "position", "job", "title",
        "tasks", "duties", "requirements", "responsibilities", "functions",
        "expected", "ensure", "develop", "provide", "manage", "team", "individual",
        "company", "employer", "candidate", "applicant", "opportunity", "apply","organization","resume","resumes"
        "years", "year", "months", "month", "days", "day", "hours", "hour",
        # Diversity, Inclusion, and Equality Terms
        "diversity", "diverse", "inclusive", "inclusion", "belonging", "equity",
        "equality", "equal", "opportunity", "commitment", "underrepresented",
        "minorities", "disability", "disabilities", "veterans", "lgbtq",
        "accessibility", "gender", "race", "ethnicity", "background",
        "culture", "respect", "fairness", "values", "mission", "vision",
        "identity", "justice", "ethnic", "collaboration", "empower", "supportive"
    ]
    sw=sw+jpsw

    text = text.lower()

    text = re.sub(r"[^a-zA-Z?.!,¿]+", " ", text) # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")

    text = re.sub(r"http\S+", "",text) #Removing URLs
    #text = re.sub(r"http", "",text)

    html=re.compile(r'<.*?>')

    text = html.sub(r'',text) #Removing html tags

    punctuations = '@#!?+&*[]-%.:/();$=><|{}^' + "'`" + '_'
    for p in punctuations:
        text = text.replace(p,'') #Removing punctuations

    text = [word.lower() for word in text.split() if word.lower() not in sw] #Removing stopwords

    text = " ".join(text) #removing stopwords

    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text) #Removing emojis

    return text

def features_encoder(data):
    encoder= LabelEncoder()
    return encoder.fit_transform(data)

def split_data(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=pm.TRAIN_SPLIT, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, train_size=pm.VAL_SPLIT, random_state=42)
    return X_train, X_test, y_train, y_test, X_val, y_val

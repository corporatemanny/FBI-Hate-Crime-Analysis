

test = [
    'Anti-Lesbian, Gay, Bisexual, or Transgender (Mixed Group)',
    'Anti-Sikh',
    'Anti-Transgender',
    'Anti-Gay (Male)',
    'Anti-White',
    'Anti-American Indian or Alaska Native;Anti-Female;Anti-Hispanic or Latino',
    'Anti-Gay (Male)',
    'Anti-Catholic',
    'Anti-White',
    'Anti-Asian',
    'Anti-White',
    'Anti-Gay (Male)',
    'Anti-Hispanic or Latino',
    'Anti-Black or African American',
    'Anti-Lesbian, Gay, Bisexual, or Transgender (Mixed Group)'
        ]

def desc_count(arr):

    tally = {'Race': 0, 'LGBTQ': 0, 'Religion': 0, 'Disablity': 0, 'Gender': 0, 'Unknown': 0 }

    race_desc = [
        'Anti-White',
        'Anti-Black or African American',
        'Anti-Hispanic or Latino',
        'Anti-Other Race/Ethnicity/Ancestry',
        'Anti-Asian',
        'Anti-Multiple Races, Group',
        'Anti-Arab',
        'Anti-American Indian or Alaska Native',
        'Anti-Native Hawaiian or Other Pacific Islander',
    ]

    lgbtq = [
        'Anti-Lesbian, Gay, Bisexual, or Transgender (Mixed Group)',
        'Anti-Gender Non-Conforming',
        'Anti-Gay (Male)',
        'Anti-Lesbian (Female)',
        'Anti-Transgender',
        'Anti-Bisexual',
        'Anti-Heterosexual',
    ]

    religion = [
        'Anti-Jewish',
        'Anti-Islamic (Muslim)',
        'Anti-Catholic',
        'Anti-Multiple Religions, Group',
        'Anti-Protestant',
        'Anti-Atheism/Agnosticism',
        "Anti-Jehovah's Witness",
        'Anti-Other Christian',
        'Anti-Other Religion',
        'Anti-Hindu',
        'Anti-Buddhist',
        'Anti-Church of Jesus Christ',
        'Anti-Eastern Orthodox (Russian, Greek, Other)',
        'Anti-Sikh'
    ]

    disability = [
        'Anti-Mental Disability',
        'Anti-Physical Disability'
    ]

    gender = [
        'Anti-Female',
        'Anti-Male'
    ]

    unknown = [
        "Unknown (offender's motivation not known)"
    ]

    for description in arr:
        split_desc = description.split(';')
        for category in split_desc:
            if category in race_desc:
                tally['Race'] += 1
            elif category in religion:
                tally['Religion'] += 1
            elif category in lgbtq:
                tally['LGBTQ'] += 1
            elif category in disability:
                tally['Disablity'] += 1
            elif category in gender:
                tally['Gender'] += 1
            else:
                tally['Unknown'] += 1
    
    return tally
            
print(desc_count(test))







# import re 

# def replace(text):

#     replace_patterns = [
#         (r'\bAnti-Black\b', 'Racially Motivated'),
#         (r'\bAnti-Arab\b', 'Racially Motivated'),
#         (r'\bAnti-Hispanic\b', 'Racially Motivated'),
#         (r'\bAnti-Black or African American;Anti-Gay (Male)\b', 'Racially Motivated')
#     ]

#     for pattern, replacement in replace_patterns:
#         if re.search(pattern, text):
#             text = re.sub(pattern, replacement, text)

#     return text
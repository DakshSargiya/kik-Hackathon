import json
import process.courseName as cn
import process.courses as c
import pandas


def getOptions(goals: list) -> list:
    """
    enter goals to send the goals of the student
    impCG to send if student wants to improve CG or go for intrest
    """
    with open('breadth_course.json') as f:
        bcjson = json.load(f)

    df = pandas.read_csv('final_data.csv')

    dictCourse = {}

    for x in c.courses:
        dictCourse[x] = 0

    options = []
    final = []
    for goal in goals:
        with open(f'./fieldsjson/{goal}.json') as file:
            x = json.load(file)
            for i in x:
                dbx = []
                try:
                    y = c.courses
                    z = cn.couseName
                    cid = y[cn.couseName.index(i)]

                    name = z[cn.couseName.index(i)]
                    csvdata = df.loc[df['cid'] == cid]
                    ltp = bcjson[cid]["L-T-P"]
                    # print(cid, "Percentage: ", x[i], "L-T-P: ", ltp)
                    dictCourse[cid] += x[i]
                    for a, b in csvdata.iterrows():
                        dbx.append({'EX': b['EX'], 'A': b['A'], 'B': b['B'], 'C': b['C'],
                                   'D': b['D'], 'P': b['P'], 'F': b['F'], 'session': b['session']})
                    # print(dbx)
                except Exception as e:
                    print(e)

                avg = 0
                for row in dbx:
                    avg += (row['EX']*10 + row['A']*9 + row['B']*8 + row['C']*7 + row['D']*6 + row['P']*5)/(
                        row['EX'] + row['A'] + row['B'] + row['C'] + row['D'] + row['P'] + row['F'])
                if (len(dbx)):
                    avg = avg/(len(dbx))
                options.append({'cid': cid,
                                'L-T-P': ltp,
                                'name': name,
                                'prevData':
                                {'data': dbx,
                                 "avg":  avg
                                 }
                                })

    for i in options:
        i['percent'] = dictCourse[i['cid']] / len(goals)
        final.append(i)

    return final


# print(getOptions(['Aerospace Engineer', 'Cybersecurity Analyst']))

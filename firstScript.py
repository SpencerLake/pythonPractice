print('hello world')

#print((5+10) * (9/2))

new_var = "villian"

#print(type(new_var))

practice_str = 5

#print(type(practice_str))


practice_str = 'This is supposed to be long'
prac_str_2 = 'Messing with line \n breaks'



#print(len(practice_str))
#print(prac_str_2[5])
#print(prac_str_2[-2])

#print(type(practice_str))


# Can use a third parameter for 'step size', which iterations to grab 
#print(practice_str[3:10])
#print(practice_str[:10])
#print(practice_str[::2])
#print(practice_str[3:10])


prac_conc = 'Pam'

#print('D' + prac_conc[1:] + 'n')
#print(prac_conc * 2)

#variables can have methods attached much like other languages

new_prac_conc = prac_conc.upper()
#print(new_prac_conc)


#You can turn na string into an array/list
#print(practice_str.split())
#print(practice_str.split('s'))

format_test = 'BLAM'
amount_var = 'THIS'

#print('Fancy fancy way to insert this, {}, into my string'.format('Hello All'))
#print('Testing order of these nifty inserts, 1({2}), 2({0}), 3({1}). And there you go'.format('This', 'Out', 'Testing'))
#print('Testing order of these nifty inserts, 1({2}), 2({1}), 3({2}). And there you go'.format('This', format_test, 'Testing'))
#print('Testing order of these nifty inserts, 1({c}), 2({a}), 3({b}). And there you go'.format(c='This', b=format_test, a='Testing'))
#print(f'Another test, realizing how intensive python can be. About {amount_var} much')


#List stuff

prac_list = ['One', 'Two', 'Three', 'Four']
prac_list[0] = 'ONE'
#print(prac_list)
prac_list.append('Five')
#print(prac_list)
#print(prac_list.pop())
#print(prac_list)
prac_list2 = prac_list.pop(0)
#print(prac_list2)
#print(prac_list)


prac_list3 = ['e', 'b', 'd', 'c', 'a']
pract_list4 = [1,2,3,4]

prac_list3.sort()
sorted_list = prac_list3
#print(sorted_list)
prac_list3.reverse()
sorted_rev = prac_list3
#print(sorted_rev)


#DICTIONARIES

first_dict = {'key1':'first value', 'key2':'second value'}
#print(first_dict['key1'])

sec_dict = {'k1':'simple', 'k2':1234, 'k3':[1,2,3,4], 'k4':{'innerKey':321}}
#print(sec_dict['k2'])
#print(sec_dict['k4']['innerKey'])
#print(sec_dict['k3'][2])




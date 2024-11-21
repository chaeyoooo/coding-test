# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=


# def croatia_alphabet():
#     croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#     word = input()
#     for i in croatia:
#         word = word.replace(i,'1')
#         print(len(word))

# croatia_alphabet()


dict = {'c=':1, 'c-':1, 'dz=':1, 'd-':1, 'lj':1, 'nj':1, 's=':1, 'z=':1}
word = input()
for key in dict.keys():
    word = word.replace(key, '1')
print(len(word))
# polyglots

allKnownLang = set()
someKnownLang = set()

nSchoolboys = int(input())
for i in range(nSchoolboys):
    nLanguages = int(input())
    language = set()
    for j in range(nLanguages):
        language.add(input())
    if i == 0:
        allKnownLang.update(language)
    else:
        allKnownLang.intersection_update(language)
    someKnownLang.update(language)
    # print(i, j, allKnownLang, someKnownLang)
print(len(allKnownLang))
print('\n'.join(allKnownLang))
print(len(someKnownLang))
print('\n'.join(someKnownLang))

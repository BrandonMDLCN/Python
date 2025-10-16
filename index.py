def high(x):
    defragmentar = list(str(x));
    multiplicador = len(defragmentar);
    expandedForm = ''
    for i in range(len(defragmentar)):
        defragmentar[i] = defragmentar[i]+('0'*(multiplicador-1))
        multiplicador -= 1;
        if defragmentar[i] != '0'*(len(defragmentar[i])):
            expandedForm += defragmentar[i] + ' + '
    expandedForm = expandedForm[:-3]
    return expandedForm
print(high(70304))
class buttonHandler():
    def write_number(self, number, label, display_2, save_operation):
        print(0, save_operation)
        if (label.text() == '0' or label.text() == '0.0' or label.text() == 'Division by zero!' or
                (save_operation != [] and save_operation[-1] in '/*-+') or save_operation == []):
            label.setText(number)
            save_operation.append(number)
        else:
            label.setText(label.text() + number)
            save_operation.append(number)
        if len(save_operation) >= 2 and save_operation[0] == '0' and save_operation[1] != '.':
            del save_operation[0]
        display_2(save_operation)

    def func_operation(self, operation, label, display_2, save_operation):
        print('?', save_operation)
        if len(save_operation) == 0 and operation == '-':
            save_operation.append(operation)
            label.setText(operation)
        elif len(save_operation) > 0:
            if save_operation[-1] in '0123456789':  # если последняя цифра - вводится операция
                save_operation.append(operation)
            else:  # если последний опeранд - он заменяется
                save_operation[-1] = operation
        else:
            label.setText('0')
        display_2(save_operation)

    def func_del(self, label, display_2, save_operation):
        if label.text() != '0':
            if len(label.text()) > 1:
                label.setText(label.text()[:-1])
                if len(save_operation) != 0 and save_operation[-1] not in '*-+/':
                    del save_operation[-1]
            else:
                label.setText('0')
                if len(save_operation) != 0 and save_operation[-1] not in '*-+/':
                    del save_operation[-1]
            display_2(save_operation)
            print(save_operation)


    def func_c(self, label, display_2, save_operation):
        save_operation.clear()
        label.setText('0')
        display_2(['0'])

    def func_dot(self, label, save_operation):  # ця хуйня вроде работает
        flag = False
        if len(save_operation) > 0:
            # -------------------------------------------
            for x in reversed(save_operation):
                if x not in '/*-+':
                    if x == '.':
                        flag = True
                        break
                    else:
                        continue
                else:
                    break
            # --------------------------------------------
            if flag == False and save_operation[-1] in '0123456789':
                save_operation.append('.')
                label.setText(label.text() + '.')
            elif flag == False and save_operation[-1] not in '0123456789':
                save_operation.append('0')
                save_operation.append('.')
                label.setText('0.')
        else:  # ця херня работает
            save_operation.append('0')
            save_operation.append('.')
            label.setText('0.')

    def func_percent(self, label, display_2, save_operation):
        # функция процента
        counter = 0
        first_operand = []
        if save_operation != [] and save_operation[-1] not in '/*-+':
            for x in reversed(save_operation):
                if x not in '-+*/':
                    counter += 1
                else:
                    break
            percent = save_operation[-counter:]  # второе число 20
            print(save_operation)
            for i in range(counter):
                del save_operation[-1]
            print(save_operation, counter)
            oper = save_operation.pop(-1)
            for x in reversed(save_operation):
                if x not in '-+*/':
                    first_operand += x
                else:
                    break
            first_operand = (float(''.join(reversed(first_operand))))  # первое число лист 60
            percent_digit = ''.join(percent)
            itog = (float(first_operand / 100) * float(percent_digit))
            save_operation.append(oper)
            save_operation.extend(str(round(itog, 3)))
            label.setText(str(round(itog, 3)))
            display_2(save_operation)

    def func_equal(self, label, display_2, save_operation):
        if save_operation != []:
            result = ''
            result += ''.join(save_operation)
            index_zero = result.find('/0')
            if '/0' in result and result[index_zero+1:index_zero+3] != '0.':
                label.setText('Division by zero!')
                save_operation.clear()
            else:  # проверка на окончание и начало со знака
                if result[0] not in '-0123456789':
                    result = result[1:]
                if result[-1] not in '0123456789':
                    result = result[:-1]
                result_it = eval(result)
                label.setText(str(result_it))
                display_2(list(result))
                save_operation.clear()

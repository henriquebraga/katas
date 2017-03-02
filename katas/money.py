#-*- coding: utf-8 -*-
"""Ler o total pago e valor efetivamente pago, informando o menor 
número de cédulas e moedas que devem ser fornecidas como troco.

"""
import copy


def calculate_money(to_be_paid, paid):
	change = paid - to_be_paid
	message = ''

	if paid - to_be_paid == 0:
		return 'Sem cédulas. Valor pago é exatamente igual.'

	if change >= 100:
		message, change = count_paper_money_value_for_change(
			change=change,
			paper_money_value=100,
			message=message
			)

	if change >= 50:
		message, change = count_paper_money_value_for_change(
			change=change,
			paper_money_value=50,
			message=message
			)
	
	if change >= 10:
		message, change = count_paper_money_value_for_change(
			change=change,
			paper_money_value=10,
			message=message
			)		

	if change >= 5:
		message, change = count_paper_money_value_for_change(
			change=change,
			paper_money_value=5,
			message=message
			)		

	if change >= 1:
		message, change = count_paper_money_value_for_change(
			change=change,
			paper_money_value=1,
			message=message
			)

	return message


def count_paper_money_value_for_change(
	change,
	paper_money_value,
	message=''
	):
	quantity, change_remaining = divmod(change, paper_money_value)
	message = format_paper_money_message(quantity, paper_money_value, message)
	return message, change_remaining


def format_paper_money_message(quantity, paper_money_value, message):	
	_message = copy.copy(message)

	if _message:
		_message += ', '

	_message += 'Cédulas de R${value}: {quantity}'.format(
		value=paper_money_value,
		quantity=quantity
		)

	return _message


if __name__ == '__main__':
	assert calculate_money(to_be_paid=100, paid=100) == 'Sem cédulas. Valor pago é exatamente igual.'
	assert calculate_money(to_be_paid=150, paid=150) == 'Sem cédulas. Valor pago é exatamente igual.'

	assert calculate_money(to_be_paid=200, paid=300) == 'Cédulas de R$100: 1'
	assert calculate_money(to_be_paid=300, paid=400) == 'Cédulas de R$100: 1'

	assert calculate_money(to_be_paid=400, paid=600) == 'Cédulas de R$100: 2'
	assert calculate_money(to_be_paid=500, paid=700) == 'Cédulas de R$100: 2'

	assert calculate_money(to_be_paid=500, paid=800) == 'Cédulas de R$100: 3'

	assert calculate_money(to_be_paid=100, paid=150) == 'Cédulas de R$50: 1'
	assert calculate_money(to_be_paid=200, paid=250) == 'Cédulas de R$50: 1'

	assert calculate_money(to_be_paid=150, paid=160) == 'Cédulas de R$10: 1'
	assert calculate_money(to_be_paid=170, paid=180) == 'Cédulas de R$10: 1'

	assert calculate_money(to_be_paid=150, paid=170) == 'Cédulas de R$10: 2'
	assert calculate_money(to_be_paid=160, paid=180) == 'Cédulas de R$10: 2'

	assert calculate_money(to_be_paid=150, paid=180) == 'Cédulas de R$10: 3'
	assert calculate_money(to_be_paid=140, paid=170) == 'Cédulas de R$10: 3'

	assert calculate_money(to_be_paid=150, paid=190) == 'Cédulas de R$10: 4'
	assert calculate_money(to_be_paid=160, paid=200) == 'Cédulas de R$10: 4'

	assert calculate_money(to_be_paid=150, paid=155) == 'Cédulas de R$5: 1'
	assert calculate_money(to_be_paid=165, paid=170) == 'Cédulas de R$5: 1'

	assert calculate_money(to_be_paid=155, paid=156) == 'Cédulas de R$1: 1'
	assert calculate_money(to_be_paid=156, paid=157) == 'Cédulas de R$1: 1'

	assert calculate_money(to_be_paid=155, paid=157) == 'Cédulas de R$1: 2'
	assert calculate_money(to_be_paid=156, paid=158) == 'Cédulas de R$1: 2'

	assert calculate_money(to_be_paid=155, paid=158) == 'Cédulas de R$1: 3'
	assert calculate_money(to_be_paid=157, paid=160) == 'Cédulas de R$1: 3'

	assert calculate_money(to_be_paid=155, paid=159) == 'Cédulas de R$1: 4'
	assert calculate_money(to_be_paid=156, paid=160) == 'Cédulas de R$1: 4'

	assert calculate_money(to_be_paid=150, paid=300) == 'Cédulas de R$100: 1, Cédulas de R$50: 1'
	assert calculate_money(to_be_paid=200, paid=350) == 'Cédulas de R$100: 1, Cédulas de R$50: 1'

	assert calculate_money(to_be_paid=200, paid=450) == 'Cédulas de R$100: 2, Cédulas de R$50: 1'

	assert calculate_money(to_be_paid=250, paid=477) == 'Cédulas de R$100: 2, Cédulas de R$10: 2, Cédulas de R$5: 1, Cédulas de R$1: 2'







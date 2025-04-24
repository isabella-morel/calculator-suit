# https://www.w3schools.com/python/ref_func_eval.asp 
# https://flet.dev/docs/controls/tabs

import flet as ft

def main(page: ft.Page):
    page.title = "Calculator Suite"

    # Calculator
    current_input = ""
    last_operation = None

    def button_clicked(e):
        nonlocal current_input, last_operation

        button_text = e.control.text

        if button_text == "AC":
            current_input = ""
            result.value = "0"

        elif button_text == "+/-":
            if current_input:
                if current_input[0] == ("-"):
                    current_input = current_input[1:]
                else:
                    current_input = "-" + current_input
                result.value = current_input

        elif button_text == "%":
            if current_input:
                current_input = str(float(current_input) / 100)
                result.value = current_input

        elif button_text == "=":
            try:
                if last_operation:
                    current_input = str(eval(current_input))
                    result.value = current_input
                    last_operation = None
            except:
                result.value = "Error"
                current_input = ""

        elif button_text in ["+", "-", "x", "/"]:
            if current_input and not current_input[-1] == (("+", "-", "x", "/")):
                current_input += button_text.replace("x", "*")
                result.value = current_input
                last_operation = button_text

        else:
            current_input += button_text
            result.value = current_input

        page.update()

    result = ft.Text(value="0", size=40, text_align=ft.TextAlign.RIGHT, width=250)
    delete_button = ft.FilledTonalButton(text="AC", on_click=button_clicked)
    change_sign = ft.FilledTonalButton(text="+/-", on_click=button_clicked)
    percent = ft.FilledTonalButton(text="%", on_click=button_clicked)
    divide = ft.FilledTonalButton(text="/", on_click=button_clicked)
    multiply = ft.FilledTonalButton(text="x", on_click=button_clicked)
    subtract = ft.FilledTonalButton(text="-", on_click=button_clicked)
    add = ft.FilledTonalButton(text="+", on_click=button_clicked)
    equals = ft.FilledTonalButton(text="=", on_click=button_clicked)
    zero = ft.FilledTonalButton(text="0", width=121, on_click=button_clicked)
    one = ft.FilledTonalButton(text="1", on_click=button_clicked)
    two = ft.FilledTonalButton(text="2", on_click=button_clicked)
    three = ft.FilledTonalButton(text="3", on_click=button_clicked)
    four = ft.FilledTonalButton(text="4", on_click=button_clicked)
    five = ft.FilledTonalButton(text="5", on_click=button_clicked)
    six = ft.FilledTonalButton(text="6", on_click=button_clicked)
    seven = ft.FilledTonalButton(text="7", on_click=button_clicked)
    eight = ft.FilledTonalButton(text="8", on_click=button_clicked)
    nine = ft.FilledTonalButton(text="9", on_click=button_clicked)
    decimal = ft.FilledTonalButton(text=".", on_click=button_clicked)

    # Currency Converter
    exchange_rates = {
    "Dominican Peso": {"US Dollar": 0.017, "Euro": 0.015, "Japanese Yen": 2.4, "British Pound": 0.013, "Dominican Peso": 1},
    "US Dollar": {"Dominican Peso": 58.82, "Euro": 0.85, "Japanese Yen": 130.5, "British Pound": 0.72, "US Dollar": 1},
    "Euro": {"Dominican Peso": 66.67, "US Dollar": 1.18, "Japanese Yen": 153.5, "British Pound": 0.85, "Euro": 1},
    "Japanese Yen": {"Dominican Peso": 0.42, "US Dollar": 0.0077, "Euro": 0.0065, "British Pound": 0.0057, "Japanese Yen": 1},
    "British Pound": {"Dominican Peso": 76.92, "US Dollar": 1.39, "Euro": 1.18, "Japanese Yen": 175.5, "British Pound": 1}}

    currency_to = ft.Dropdown(
        label="Currency to convert to", 
        options=[
            ft.dropdown.Option("Dominican Peso"),
            ft.dropdown.Option("US Dollar"),
            ft.dropdown.Option("Euro"),
            ft.dropdown.Option("Japanese Yen"),
            ft.dropdown.Option("British Pound")
        ])

    currency_from = ft.Dropdown(
        label="Currency to convert from", 
        options=[
            ft.dropdown.Option("Dominican Peso"),
            ft.dropdown.Option("US Dollar"),
            ft.dropdown.Option("Euro"),
            ft.dropdown.Option("Japanese Yen"),
            ft.dropdown.Option("British Pound")
        ])

    def convert_currency(e):
        try:
            amount = float(currency_input.value)
            from_currency = currency_from.value
            to_currency = currency_to.value

            if from_currency and to_currency:
                rate = exchange_rates[from_currency][to_currency]
                converted = amount * rate
                currency_result.value = f"{converted} {to_currency}"
            else:
                currency_result.value = "Please select both currencies"
        except:
            currency_result.value = "Invalid input"
        
        currency_result.update()

    convert_button = ft.ElevatedButton(text="Convert", on_click=convert_currency)
    currency_input = ft.TextField(label="Enter amount to convert")
    currency_result = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    # Unit Converter
    unit_conversion_rates = {
        "Meters": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701},
        "Kilometers": {"Meters": 1000, "Kilometers": 1, "Miles": 0.621371, "Feet": 3280.84, "Inches": 39370.1},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Miles": 1, "Feet": 5280, "Inches": 63360},
        "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394, "Feet": 1, "Inches": 12},
        "Inches": {"Meters": 0.0254, "Kilometers": 0.0000254, "Miles": 0.000015783, "Feet": 0.0833333, "Inches": 1},}

    unit_from = ft.Dropdown(
        label="Unit to convert from",
        options=[
            ft.dropdown.Option("Meters"),
            ft.dropdown.Option("Kilometers"),
            ft.dropdown.Option("Miles"),
            ft.dropdown.Option("Feet"),
            ft.dropdown.Option("Inches"),
        ])

    unit_to = ft.Dropdown(
        label="Unit to convert to",
        options=[
            ft.dropdown.Option("Meters"),
            ft.dropdown.Option("Kilometers"),
            ft.dropdown.Option("Miles"),
            ft.dropdown.Option("Feet"),
            ft.dropdown.Option("Inches"),
        ])

    unit_input = ft.TextField(label="Enter value to convert")
    unit_result = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def convert_unit(e):
        try:
            value = float(unit_input.value)
            from_unit = unit_from.value
            to_unit = unit_to.value

            if from_unit and to_unit:
                rate = unit_conversion_rates[from_unit][to_unit]
                converted_value = value * rate
                unit_result.value = f"{converted_value} {to_unit}"
            else:
                unit_result.value = "Please select both units"
        except:
            unit_result.value = "Invalid input"

        unit_result.update()

    convert_unit_button = ft.ElevatedButton(text="Convert", on_click=convert_unit)

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Calculator",
                content=ft.Column([
                        ft.Row([result]),
                        ft.Row([delete_button, change_sign, percent, divide]),
                        ft.Row([seven, eight, nine, multiply]),
                        ft.Row([four, five, six, subtract]),
                        ft.Row([one, two, three, add]),
                        ft.Row([zero, decimal, equals]),
                    ])),
            ft.Tab(text="Currency Converter", content=ft.Column([
                ft.Row([currency_result]),
                ft.Row([currency_from, currency_to]),
                ft.Row([currency_input]),
                ft.Row([convert_button]),
                ])),
            ft.Tab(text="Unit Converter", content=ft.Column([
                    ft.Row([unit_result]),
                    ft.Row([unit_from, unit_to]),
                    ft.Row([unit_input]),
                    ft.Row([convert_unit_button]),
                ]))
        ])
    # for some reason when I try to center it the content just disappears... so no centering :)

    page.add(tabs)

ft.app(main)
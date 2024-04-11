Feature: APITest

  Scenario Outline: test <CurrencyConversionTestCase>
    Given url 'https://some-page.com/currency-conversion'
    When request {"<sourceCurrency>": <Source>,"<targetCurrency>": <Target>,"<specificDate>": <Date>}
    And method (GET,POST,...)
    And match response.exchangeRate == <exchangeRate>
    And match response.errorMessage == <errorMessage>
    Then status 200
    Examples:
    |TestCase|sourceCurrency|Source   |targetCurrency|Target   |specificDate|Date      |exchangeRate|errorMessage                   |
    |CC01    |sourceCurrency|currencyA|targetCurrency|currencyB|specificDate|01/01/2020|rate        |null                           |
    |CC02    |sourceCurrency|currencyA|targetCurrency|         |specificDate|01/01/2020|null        |"Enter a valid source Currency"|
    |CC03    |sourceCurrency|         |targetCurrency|currencyB|specificDate|01/01/2020|null        |"Enter a valid target Currency"|
    |CC04    |sourceCurrency|         |targetCurrency|         |specificDate|01/01/2020|null        |"Currency fields are empty"    |
    |CC05    |sourceCurrency|currencyA|targetCurrency|currencyB|specificDate|          |null        |"Enter a valid date"           |
    |CC06    |sourceCurrency|currencyA|targetCurrency|wrongB   |specificDate|01/01/2020|null        |"Enter a valid source Currency"|
    |CC07    |sourceCurrency|wrongA   |targetCurrency|currencyB|specificDate|01/01/2020|null        |"Enter a valid target Currency"|
    |CC08    |sourceCurrency|wrongA   |targetCurrency|wrongB   |specificDate|01/01/2020|null        |"Currency fields are invalid"  |
    |CC09    |sourceCurrency|currencyA|targetCurrency|currencyB|specificDate|2020/01/01|null        |"Enter a valid date"           |
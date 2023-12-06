# IODog-API

O projeto pode está localizado no seguinte link:

http://eokelvio.pythonanywhere.com/ <br>

<h3>Instruções de Uso</h3> <br>

- Manipulação de horários:<br><br>


Criar horários de alimentação : envie um JSON no método POST com o valor {“Times”:”hh:mm”}(hora e minutos) para este endpoint(link): (https://eokelvio.pythonanywhere.com/hours/).

Para listar os horários faça uma requisição do método GET para este endpoint(link): (https://eokelvio.pythonanywhere.com/hours/).

Você pode atualizar ou deletar um horário específico usando os métodos PUT ou DELETE respectivamente indicando o ID no fim da URL. ex: (https://eokelvio.pythonanywhere.com/hours/1/).<br><br>


- Cadastro de LOGs:<br><br>


Para cadastrar um LOG deve-se enviar um JSON para com os seguintes parâmetros

    {
        "food_liberation": true, /Se a ração foi liberada ou não
        "portions": 2, /Quantidade de porções liberadas
        "food_level": "75%", /Quantia de ração ainda disponível
    }
<br><br> 
JSON esse que deve ser enviado ao endpoint(link): https://eokelvio.pythonanywhere.com/log/

A listagem ocorre usando o método GET no link: https://eokelvio.pythonanywhere.com/log/<br><br>

- Uso do FeedTime:<br><br>

As informações para o uso do ESP32 estão disponíveis no link: https://eokelvio.pythonanywhere.com/feedTimes/1/ atraves do uso de um GET.
O JSON retornado por este link lhe dá as informações de quantidade de porções, horário atual e horários de alimentação.

<br>
<h3>Exemplos de Uso</h3><br>


"hours": "http://eokelvio.pythonanywhere.com/hours/"
  
  - POST
     
      Entrada:
    
        {
          "times": "16:00"
        }
    
      Saida:
    
        [
          {
            "id":1,
            "times":"16:00"
          }
        ]
    
  - GET
    
      "http://eokelvio.pythonanywhere.com/hours/1/"
    
  - PUT
    
      "http://eokelvio.pythonanywhere.com/hours/1/"
    
      Entrada:
      
          {
            "times":"18:00"
          }
  
      Saida:
      
          {
            "id":1,    
            "times":"18:00"
          }
    
<br><br>
"log": "http://eokelvio.pythonanywhere.com/log/"<br><br>

  - POST
  
      Entrada:
        
            {
              "food_liberation": true,
              "portions": 1,
              "food_level": "75"
            }
      
      Saida:
        
            [
               {
                 "id": 1,
                 "food_liberation": true,
                 "portions": 1,
                 "food_level": "75",
                 "created_at": "2023-12-04T19:30:43.835802Z"
               }
            ]
    
  - GET
      
        "http://eokelvio.pythonanywhere.com/log/1/"

  - PUT

        "http://eokelvio.pythonanywhere.com/log/1/"

        Entrada:
        
            {
              "food_liberation": false,
              "portions": 2,
              "food_level": "60"
            }
  
        Saida:
  
            [
              {
                "id": 1,
                "food_liberation": false,
                "portions": 2,
                "food_level": "60",
                "created_at": "2023-12-04T20:39:43.835802Z"
              }
            ]

<br><br>
"feedTimes": "http://eokelvio.pythonanywhere.com/feedTimes/"<br><br>

  - POST
  
      Entrada:
        
            {
              "portion": 1
            }
      
      Saida:
      
            [
               {
                  "id": 1,
                  "portion": 1,
                  "current_time": "2023-12-04T17:34:26.347530Z",
                  "feed_time": [
                      "16:00",
                      "20:00",
                      "18:30"
                  ]
               }
            ]

  - GET

      "http://eokelvio.pythonanywhere.com/feedTimes/1/"

  - PUT

      "http://eokelvio.pythonanywhere.com/feedTimes/1/"

      Entrada:

        {
          "portion": 3
        }

      Saida:

        [
          {
            "id": 1,
            "portion": 1,
            "current_time": "2023-12-04T17:34:26.347530Z",
            "feed_time": [
                "16:00",
                "20:00",
                 "18:30"
              ]
           }
        ]
        

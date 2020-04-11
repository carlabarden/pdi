## Entrega 1 - PDI

Sistema que verifica garrafas não-cheias em uma linha de produção.

---
### Introdução

Em Processamento de Imagens, operações realizadas no domínio espacial consistem na manipulação direta de cada pixel que compõe a imagem. Matematicamente,
$$g(x, y) = T[f(x, y)]$$, onde: 
$$g(x,y)$$ é a imagem de saída;
$$f(x,y)$$ é a imagem de entrada e 
$$T$$ é o operador. 

No caso onde $$g$$ depende apenas do valor de $$f$$ em um único ponto $$(x,y)$$, $$T$$ é dito uma **Função de Transformação de Intensidade** , sendo apresentada na forma:
$$s=T(r)$$, onde:
$$s$$ e $$r$$ são variáveis que indicam a intensidade de $$g$$ e $$f$$ em qualquer ponto $$(x,y)$$.

Uma das possíveis aplicações desse tipo de operação é o *realce* de características relevantes da imagem, de forma que a imagem transformada seja mais adequada à aplicação que se destina do que a imagem original.

---
###Problema proposto

Implementar um sistema que permita identificar uma garrafa que não está corretamente cheia. As imagens proporcionadas são capituradas por uma câmera fixa, em escala de cinzas e diretamente da linha de produção.
Adicionalmente, espera-se que o sistema possa:
 - Identificar uma garrafa não-cheia em qualquer posição da imagem;
 - Indicar a posição da garrafa na imagem;
 - Informar a porcentagem que a garrafa não-cheia contém

![Garrafas](../fig/botellas.tif)

---

###Sistema

---


####Referências
Videoaulas da Disciplina;
Processamento Digital de Imagens - Rafael C. Gonzalez e Richard E. Woods - 3a edição.


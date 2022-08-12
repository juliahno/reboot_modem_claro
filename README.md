## Script para reboot do modem Claro Kaon CG3000

Para uso do script é necessário informar **MD5_USUARIO** e **MD5_SENHA**.<br>
O conteúdo destas variáveis pode ser obtido a partir da função MD5* contida no arquivo Javascript da página do modem (http://192.168.0.1).

Pode-se acessar o resultado do processamento, pela função MD5, de uma das formas abaixo:

- **Opção 1**
1. A partir da página inicial do modem, abra a console de desenvolvedor (CTRL+SHIFT+I);
2. Clique na aba "Console" e digite o nome da função e informe usuário e senha como no seguinte exemplo:<br><br>
   ![image](https://user-images.githubusercontent.com/43688750/184453309-4be7f8fa-4253-414b-aa75-01cffe98333d.png)

- **Opção 2**
1. A partir da página inicial do modem, abra a console de desenvolvedor (CTRL+SHIFT+I);
2. Clique na aba "Network";
3. Logue-se normalmente na página;
4. Na console de desenvolvedor, localize "logincheck.cmd" e clique sobre o nome;
5. Clique na aba "Payload" e os dados deverão estar disponíveis

<br>
*A função MD5 citada não produz os *hashes* da função criptográfica de mesmo nome. 

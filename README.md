# Detecção de Rostos em Tempo Real com OpenCV e MediaPipe

Este projeto utiliza o OpenCV e o MediaPipe para detectar rostos em tempo real a partir da câmera web do usuário. O código foi desenvolvido para contar a quantidade de rostos detectados e exibir essa contagem em tempo real no vídeo da webcam.

## Aplicações Práticas

Este projeto pode ser utilizado em diversas aplicações que requerem reconhecimento facial em tempo real, como:

- **Sistemas de segurança e monitoramento**: Detectar a presença de pessoas em um ambiente.
- **Interação com o usuário**: Monitoramento de gestos ou detecção de rostos para personalizar a experiência.
- **Contagem de pessoas**: Em ambientes como lojas, eventos ou outras áreas onde a contagem de pessoas em tempo real seja necessária.
- **Desenvolvimento de aplicativos de realidade aumentada**: Onde o reconhecimento facial pode ser utilizado para aplicar filtros ou efeitos personalizados.

## Requisitos

Antes de executar o projeto, você precisará instalar algumas dependências. Elas são:

- **OpenCV**: Biblioteca de visão computacional para capturar o vídeo da webcam e manipular imagens.
- **MediaPipe**: Biblioteca desenvolvida pelo Google, utilizada para realizar a detecção de rostos.

## Como Rodar o Projeto

Siga os passos abaixo para rodar o projeto no seu dispositivo.

### Passo 1: Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/Paulo19961944/Contador-Rostos.git
cd Contador-Rostos
```

### Passo 2: Criar um Ambiente Virtual (Opcional, mas recomendado)
Criar um ambiente virtual ajuda a isolar as dependências do projeto. Para isso, execute:

```bash
python -m venv venv
```


**Ative o ambiente virtual:**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### Passo 3: Instalar as Dependências
Instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install opencv-python mediapipe
```

### Passo 4: Rodar o Código
Agora, você está pronto para rodar o código! Basta executar o arquivo Python:

```bash
python detecao_rostos.py
```


O código irá abrir a webcam e começar a detectar rostos. Ele irá desenhar as caixas ao redor dos rostos e exibir a quantidade de rostos detectados na tela.

### Passo 5: Parar o Código
Quando desejar parar a execução, basta pressionar a tecla ESC no teclado. Isso irá encerrar o loop e fechar a janela da webcam.

### Como Funciona
- O código usa a câmera do dispositivo para capturar o vídeo.
- O MediaPipe é utilizado para detectar rostos no vídeo em tempo real.
- A contagem de rostos detectados é atualizada e exibida na tela.
= O OpenCV é usado para desenhar as caixas ao redor dos rostos e para exibir o vídeo com a contagem de rostos.

### Contribuindo
Se você deseja contribuir com melhorias ou correções neste projeto, sinta-se à vontade para criar um pull request.

- Faça um fork do repositório.
- Crie uma branch para suas alterações (git checkout -b minha-branch).
- Comite suas alterações (git commit -am 'Adiciona nova funcionalidade').
- Envie para o repositório original (git push origin minha-branch).
- Abra um pull request.

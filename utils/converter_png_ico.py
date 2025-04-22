from PIL import Image

# Abra a imagem que você deseja converter
img = Image.open("conquista.png")  # Altere para o caminho da sua imagem

#  Salve a imagem no formato ICO
img.save("iconeC.ico", format="ICO", sizes=[(32, 32)])  # Define o tamanho do ícone (32x32 no exemplo)

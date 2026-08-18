def conectar_api(url, timeout=30, retries=3, use_ssl=True):
    return f"Conectando a {url} | timeout={timeout} | retries={retries} | use_ssl={use_ssl}"
  
resultado1 = conectar_api("https://api.empresa.com")
print(resultado1)

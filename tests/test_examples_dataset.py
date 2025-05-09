from app.sentiment import analyze_sentiment

exemplos = [
    ("Ana Silva", "O atendimento foi rápido e eficiente, mas senti que poderia ser mais detalhado em alguns pontos técnicos. Por exemplo, ao explicar a falha que ocorreu, o atendente não conseguiu detalhar a causa raiz do problema, o que me deixou com dúvidas sobre o que realmente aconteceu. No geral, foi uma experiência satisfatória, mas acredito que poderia ser mais completa.", "neutra"),
    ("Bruno Souza", "Estou extremamente satisfeito com o suporte! Resolveram meu problema de forma ágil e com clareza nas explicações. Além de resolverem o erro no sistema que estava impedindo a execução de uma função crítica para o meu negócio, eles ainda sugeriram melhorias para evitar que o problema ocorresse novamente. O atendimento foi muito acima do esperado!", "positiva"),
    ("Carlos Pereira", "O serviço foi muito demorado e o atendente parecia completamente despreparado. Precisei repetir meu problema várias vezes, e mesmo assim senti que ele não estava entendendo o que eu estava dizendo. Perdi muito tempo, e o pior de tudo é que o problema não foi resolvido ao final. Vou reconsiderar continuar usando esse serviço.", "negativa"),
    ("Daniela Rocha", "A equipe de suporte foi extremamente atenciosa e dedicada. Adorei o atendimento, pois desde o início até a resolução do meu problema fui informado de cada etapa do processo. Eles fizeram de tudo para que eu entendesse o que estava acontecendo e até me ofereceram um acompanhamento extra para garantir que tudo estivesse funcionando corretamente após a solução.", "positiva"),
    ("Eduardo Lima", "Infelizmente, não conseguiram resolver meu problema, e fiquei muito decepcionado. Além da demora para obter uma resposta clara, não houve um acompanhamento adequado após o primeiro contato, o que deixou a sensação de que meu problema não era uma prioridade. Esperava mais de uma empresa com uma reputação tão boa no mercado.", "negativa"),
    ("Fernanda Carvalho", "O sistema que utilizo tem funcionado bem, mas o suporte não foi tão eficiente quanto eu esperava. Tive que esperar bastante tempo por uma resposta e, quando ela finalmente veio, não era clara o suficiente para que eu pudesse seguir as instruções por conta própria. A experiência foi mediana, espero que melhorem essa parte do serviço.", "neutra"),
    ("Gabriel Costa", "Ótimo serviço! A equipe de suporte foi muito prestativa e realmente se dedicou a resolver o meu problema. Além de solucionarem a questão com rapidez, eles ainda se certificaram de que eu entendesse o que havia causado o erro e como evitar que ele ocorresse novamente no futuro. Superou completamente as minhas expectativas.", "positiva"),
    ("Helena Ribeiro", "O atendente foi educado e respeitoso durante todo o processo, mas infelizmente não conseguiu solucionar o problema técnico que eu estava enfrentando. Ele tentou várias abordagens, mas ao final, ainda fiquei sem uma solução definitiva. Agradeço pelo esforço, mas o resultado final me deixou frustrado.", "neutra"),
    ("Igor Almeida", "Não tive uma boa experiência. Precisei contatar o suporte diversas vezes até que uma solução adequada fosse finalmente apresentada. A falta de consistência nas respostas e a demora entre os contatos me deixaram bastante insatisfeito. Era um problema simples de configuração, mas o processo todo acabou tomando muito mais tempo do que o necessário.", "negativa"),
    ("Julia Martins", "Fui muito bem atendido desde o início, e o problema foi resolvido sem nenhuma complicação. O serviço foi prático, eficiente e me surpreendeu pela rapidez com que conseguiram resolver tudo. A comunicação também foi excelente, me mantendo informado a cada passo. Um atendimento realmente de qualidade.", "positiva"),
]


def test_classificador_com_dados_do_anexo():
    erros = []

    for nome, texto, esperado in exemplos:
        detectado = analyze_sentiment(texto)
        if detectado != esperado:
            erros.append((nome, esperado, detectado))

    acertos = len(exemplos) - len(erros)

    print(f"\nAcertos: {acertos}/{len(exemplos)}\n")
    for nome, esperado, detectado in erros:
        print(f"❌ {nome}: esperado={esperado} | detectado={detectado}")

    # Se mais da metade for erro, falha o teste
    assert acertos >= len(exemplos) * 0.5, "Classificador falhou em mais de 50% dos exemplos do anexo"

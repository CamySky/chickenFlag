import random
import pygame
from data.script.botao import Botoes

class Dicas:
    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.config = cf_game.config
        self.pais_nome = ""
        self.y = 0
        self.mostrar_pais = None

        self.imagens = [
            {
                "id": 1,
                "nome": "Brasil",
                "bandeira": "data\\img\\Brasil.bmp",
                "tips": [
                    "Localizado na América do Sul.",
                    "Possui uma grande diversidade climática, incluindo florestas tropicais, regiões semiáridas e áreas temperadas.",
                    "Apresenta uma vasta topografia, com planícies, planaltos e serras.",
                    "É o maior país da América do Sul em área territorial.",
                    "Faz fronteira com a França.",
                    "Rico em recursos naturais, como petróleo, minério de ferro e água doce.",
                    "É conhecido pela sua biodiversidade, incluindo animais como a anta e a Harpia.",
                    "Tem uma economia diversificada, com destaque para a agricultura, indústria e serviços.",
                    "Participa ativamente de organizações internacionais, como o Mercosul e a ONU.",
                    "Possui um papel importante nas negociações climáticas globais devido à sua extensa área florestal.",
                    "Possui um grande poder militar na região, sendo o país mais poderosos da América Latina.",
                    "Exerce influência política e cultural na região da América Latina.",
                    "Apresenta desafios internos relacionados à desigualdade social, crime organizado e corrupção.",
                    "Possui relações complexas com países vizinhos, especialmente no que diz respeito às fronteiras e recursos naturais.",
                    "Enfrenta desafios externos, como disputas comerciais e questões ambientais, com outros países e organizações internacionais.",
                    "É membro fundador da ONU e desempenha um papel ativo na promoção da paz e segurança internacionais.",
                    "Seus interesses nacionais incluem o desenvolvimento sustentável, a segurança energética e a ampliação de sua influência regional.",
                    "Tem alguns festivais característicos como Parintins, Festa Junina e Farroupilha .",
                    "A gastronomia é famosa por pratos como feijoada, churrasco, acarajé e brigadeiro."
                ]
            },
            {
                "id": 2,
                "nome": "Rússia",
                "bandeira": "data\\img\\Russia.bmp",
                "tips": [
                    "Localizado na Eurásia, abrangendo a Europa Oriental e a Ásia Setentrional.",
                    "Possui uma vasta gama de climas, incluindo tundra, taiga e climas continentais.",
                    "A topografia inclui montanhas como os Urais, planícies extensas e a vasta Sibéria.",
                    "É um dos maiores países do mundo em área territorial.",
                    "Faz fronteira com 14 países, incluindo China, Mongólia e Finlândia.",
                    "Rico em recursos naturais, como petróleo, gás natural e minerais.",
                    "Possui grandes reservas de água doce, com destaque para o Lago Baikal, o mais profundo do mundo.",
                    "Tem uma economia baseada principalmente na exportação de recursos naturais e na indústria pesada.",
                    "Desempenha um papel significativo em organizações internacionais como a ONU e a SCO.",
                    "Tem influência nas políticas globais, especialmente no que diz respeito à segurança e energia.",
                    "Possui um dos maiores e mais poderosos exércitos do mundo.",
                    "Exerce grande influência política e militar em diversas regiões, especialmente na Europa Oriental e na Ásia Central.",
                    "Participou da guerra da Xexenia.",
                    "Tem relações complexas com países ocidentais, especialmente em questões de segurança e direitos humanos.",
                    "Enfrenta sanções econômicas e políticas devido a conflitos internacionais.",
                    "É membro permanente do Conselho de Segurança da ONU e desempenha um papel ativo na diplomacia global.",
                    "Seus interesses nacionais incluem a segurança energética, a estabilidade regional e a manutenção de sua influência global.",
                    "As vestimentas Sarafan e Kosovorotka são tradicionais no pais",
                    "A gastronomia inclui pratos como strogonoff, pelmeni, caviar e blini."
                ]
            },
            {
                "id": 3,
                "nome": "Egito",
                "bandeira": "data\\img\\Egito.bmp",
                "tips": [
                    "Localizado no nordeste da África, com uma pequena parte no sudoeste da Ásia através da Península do Sinai.",
                    "Possui um clima desértico quente, com verões extremamente quentes e invernos suaves.",
                    "A topografia é dominada pelo Deserto do Saara e o Vale do Nilo.",
                    "É famoso pelo Rio Nilo, o rio mais longo do mundo, que atravessa o país de norte a sul.",
                    "Faz fronteira com o Mar Mediterrâneo ao norte e o Mar Vermelho ao leste.",
                    "Rico em recursos naturais, incluindo gás natural, petróleo e fosfatos.",
                    "Possui vastas áreas desérticas, mas o Vale do Nilo é altamente fértil e densamente povoado.",
                    "A economia é diversificada, com destaque para o turismo, agricultura e extração de petróleo.",
                    "É um membro importante da Liga Árabe e da União Africana.",
                    "Tem influência significativa no mundo árabe e na política do Oriente Médio.",
                    "Possui uma força militar considerável e é um dos principais exércitos da região.",
                    "Exerce influência cultural e política na região, sendo um dos países mais importantes do mundo árabe.",
                    "Enfrenta desafios internos como a instabilidade política, a pobreza e a desigualdade social.",
                    "Tem relações diplomáticas estratégicas com potências ocidentais e países do Golfo.",
                    "Enfrenta tensões externas devido a questões como o controle das águas do Nilo e conflitos regionais.",
                    "Desempenha um papel ativo nas Nações Unidas e em negociações de paz no Oriente Médio.",
                    "Seus interesses nacionais incluem a segurança regional, a estabilidade econômica e a gestão dos recursos hídricos.",
                    "Conhecido por sua herança cultural e histórica, incluindo as pirâmides, templos e a antiga civilização.",
                    "A gastronomia inclui pratos como koshari, ful medames, tahini e kebabs."
                ]
            },
            {
                "id": 4,
                "nome": "África do Sul",
                "bandeira": "data\\img\\AfricaDoSul.bmp",
                "tips": [
                    "Localizado na ponta sul do continente africano.",
                    "Possui um clima variado, incluindo mediterrâneo, subtropical e semiárido.",
                    "A topografia é diversificada, com planícies costeiras, montanhas e planaltos.",
                    "É banhado pelos oceanos Atlântico e Índico.",
                    "Faz fronteira com Namíbia, Botsuana, Zimbábue, Moçambique, Essuatíni e Lesoto.",
                    "Rico em recursos naturais como ouro, diamantes e platina.",
                    "É o maior produtor de platina e um dos maiores produtores de ouro do mundo.",
                    "A economia é a mais desenvolvida da África, com setores fortes como mineração, manufatura e serviços.",
                    "É um membro ativo da União Africana e dos BRICS.",
                    "Desempenha um papel importante na política e economia do continente africano.",
                    "Possui uma força militar bem equipada, sendo uma das mais poderosas da África.",
                    "Exerce influência regional significativa e participa de operações de manutenção da paz.",
                    "Enfrenta desafios internos como desigualdade econômica, alta taxa de criminalidade e desemprego.",
                    "Tem relações diplomáticas com muitos países, incluindo parcerias estratégicas com nações ocidentais e emergentes.",
                    "Enfrenta tensões internas relacionadas a questões sociais e políticas.",
                    "É membro das Nações Unidas e desempenha um papel ativo nas negociações internacionais.",
                    "Seus interesses nacionais incluem o desenvolvimento econômico sustentável, a redução da pobreza e a melhoria da infraestrutura.",
                    "Conhecido por sua diversidade cultural, incluindo várias línguas, tradições e práticas culturais.",
                    "A gastronomia inclui pratos como bobotie, biltong, braai e malva pudding."
                ]
            },
            {
                "id": 5,
                "nome": "Nigéria",
                "bandeira": "data\\img\\Nigeria.bmp",
                "tips": [
                    "Localizado na África Ocidental.",
                    "Possui um clima tropical, com uma estação chuvosa e uma estação seca.",
                    "A topografia inclui planícies costeiras, savanas e planaltos.",
                    "É o país mais populoso da África.",
                    "Faz fronteira com Benin, Níger, Chade e Camarões.",
                    "Rico em recursos naturais, especialmente petróleo e gás natural.",
                    "É um dos maiores produtores de petróleo do mundo e o maior da África.",
                    "A economia é diversificada, com setores como petróleo, agricultura e telecomunicações.",
                    "É um membro importante da União Africana e da OPEP.",
                    "Desempenha um papel crucial na política e economia da África Ocidental.",
                    "Possui um exército considerável e participa de várias missões de paz na África.",
                    "Exerce influência significativa na região, sendo uma potência econômica e política.",
                    "Enfrenta desafios internos como a corrupção, insegurança e tensões étnicas e religiosas.",
                    "Tem relações diplomáticas com muitos países e é um importante parceiro comercial de várias nações.",
                    "Enfrenta conflitos internos, especialmente com grupos insurgentes e terroristas.",
                    "É membro das Nações Unidas e participa ativamente de suas operações e negociações.",
                    "Seus interesses nacionais incluem a segurança interna, a estabilidade econômica e a gestão sustentável dos recursos naturais.",
                    "Conhecido por sua rica diversidade cultural, incluindo várias etnias, línguas e tradições.",
                    "A gastronomia nigeriana inclui pratos como jollof rice, pounded yam, egusi soup e suya."
                ]
            },
            {
                "id": 6,
                "nome": "Quênia",
                "bandeira": "data\\img\\Quenia.bmp",
                "tips": [
                    "Localizado na África Oriental.",
                    "Possui um clima tropical ao longo da costa, clima árido e semiárido no interior e clima temperado nas áreas elevadas.",
                    "A topografia inclui o Grande Vale do Rift, montanhas como o Monte Quênia e planícies costeiras.",
                    "É banhado pelo Oceano Índico ao sudeste.",
                    "Faz fronteira com a Etiópia, Somália, Sudão do Sul, Tanzânia e Uganda.",
                    "Rico em recursos naturais como água doce, vida selvagem e recursos minerais.",
                    "É conhecido pela sua biodiversidade e parques nacionais, como o Parque Nacional Maasai Mara.",
                    "A economia é baseada principalmente na agricultura, turismo e serviços.",
                    "É um membro importante da Comunidade da África Oriental (EAC) e da União Africana (UA).",
                    "Desempenha um papel significativo na política e economia da África Oriental.",
                    "Possui uma força militar respeitável, envolvida em missões de paz na região.",
                    "Exerce influência regional, especialmente nas questões de segurança e integração econômica.",
                    "Enfrenta desafios internos como desigualdade econômica, corrupção e tensões étnicas.",
                    "Tem relações diplomáticas com muitos países e participa ativamente em fóruns regionais e internacionais.",
                    "Enfrenta conflitos internos, como os ataques do grupo terrorista Al-Shabaab, que também opera na Somália.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem a segurança interna, o desenvolvimento econômico sustentável e a conservação ambiental.",
                    "Conhecido por sua rica cultura, que inclui diversas etnias, línguas e tradições.",
                    "A gastronomia inclui pratos como ugali, sukuma wiki, nyama choma e chapati."
                ]
            },
            {
                "id": 7,
                "nome": "Etiópia",
                "bandeira": "data\\img\\Etiopia.bmp",
                "tips": [
                    "Localizado no Chifre da África.",
                    "Possui um clima variado, incluindo clima tropical de altitude, semiárido e desértico.",
                    "A topografia inclui montanhas, planaltos e depressões, com destaque para as Montanhas Simien.",
                    "É um dos países mais antigos do mundo, com uma rica história e cultura.",
                    "Faz fronteira com a Eritreia, Djibouti, Somália, Quênia, Sudão do Sul e Sudão.",
                    "Rico em recursos naturais, como água doce, ouro e potássio.",
                    "É conhecido por sua diversidade biológica e ecossistemas únicos.",
                    "A economia é baseada principalmente na agricultura, com destaque para o café, um dos principais produtos de exportação.",
                    "É um membro importante da União Africana, que tem sua sede na capital, Adis Abeba.",
                    "Desempenha um papel significativo na política e segurança do Chifre da África.",
                    "Possui uma força militar considerável, envolvida em conflitos regionais e internos.",
                    "Exerce influência regional, especialmente nas questões de segurança e integração econômica.",
                    "Enfrenta desafios internos como conflitos étnicos e políticos, bem como a pobreza.",
                    "Tem relações diplomáticas com muitos países e participa ativamente em fóruns regionais e internacionais.",
                    "Enfrenta conflitos internos e regionais, como a guerra civil na região de Tigré e tensões com a Eritreia.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem a segurança interna, o desenvolvimento econômico e a gestão dos recursos hídricos do Rio Nilo.",
                    "Conhecido por festivais tradicionais como Timkat e Meskel, além de estilos musicais como o Ethio-jazz.",
                    "A gastronomia inclui pratos como injera, doro wat, kitfo e tibs."
                ]
            },
            {
                "id": 8,
                "nome": "Argentina",
                "bandeira": "data\\img\\Argentina.bmp",
                "tips": [
                    "Localizado no sul da América do Sul.",
                    "Possui um clima variado, incluindo clima subtropical no norte, temperado no centro e subpolar no extremo sul.",
                    "A topografia inclui as vastas planícies da Pampa, as montanhas dos Andes e a região patagônica.",
                    "É o oitavo maior país do mundo em área territorial.",
                    "Faz fronteira com o Chile, Bolívia, Paraguai, Brasil e Uruguai.",
                    "Rico em recursos naturais como petróleo, gás natural e minerais.",
                    "É conhecido por suas vastas áreas agrícolas e produção de carne bovina.",
                    "A economia é diversificada, com setores como agricultura, indústria e serviços.",
                    "É um membro importante do Mercosul e das Nações Unidas.",
                    "Desempenha um papel significativo na política e economia da América do Sul.",
                    "Possui uma força militar respeitável, envolvida em missões de paz internacionais.",
                    "Exerce influência regional, especialmente nas questões de comércio e integração econômica.",
                    "Enfrenta desafios internos como inflação, dívida externa e desigualdade social.",
                    "Tem relações diplomáticas com muitos países e participa ativamente em fóruns regionais e internacionais.",
                    "Enfrenta conflitos internos relacionados à política econômica e social.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem o desenvolvimento econômico sustentável, a redução da pobreza e a melhoria da infraestrutura.",
                    "Conhecido por festivais como a Fiesta Nacional de la Vendimia, Carnaval de Gualeguaychú e estilos musicais como o tango e a chacarera.",
                    "A gastronomia inclui pratos como asado, empanadas, choripán e doce de leite."
                ]
            },
            {
                "id": 9,
                "nome": "Chile",
                "bandeira": "data\\img\\Chile.bmp",
                "tips": [
                    "Localizado na costa oeste da América do Sul.",
                    "Possui um clima variado, incluindo clima desértico no norte, mediterrâneo no centro e oceânico no sul.",
                    "A topografia inclui a longa e estreita faixa costeira dos Andes, o deserto do Atacama e a Patagônia.",
                    "É um dos países mais longos do mundo, estendendo-se do norte árido ao sul frio.",
                    "Faz fronteira com o Peru, Bolívia e Argentina.",
                    "Rico em recursos naturais como cobre, lítio e madeira.",
                    "É o maior produtor de cobre do mundo.",
                    "A economia é diversificada, com setores como mineração, agricultura, pesca e serviços.",
                    "É um membro importante da Aliança do Pacífico e das Nações Unidas.",
                    "Desempenha um papel significativo na política e economia da América Latina.",
                    "Possui uma força militar moderna e profissional.",
                    "Exerce influência regional, especialmente nas questões de comércio e integração econômica.",
                    "Enfrenta desafios internos como desigualdade econômica e questões ambientais.",
                    "Tem relações diplomáticas com muitos países e participa ativamente em fóruns regionais e internacionais.",
                    "Enfrenta conflitos internos relacionados a questões de terras indígenas e direitos sociais.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem o desenvolvimento econômico sustentável, a proteção ambiental e a melhoria da infraestrutura.",
                    "Conhecido por festivais como La Tirana e Fiesta de La Vendimia e estilos musicais como cueca e música andina.",
                    "A gastronomia inclui pratos como pastel de choclo, empanadas, cazuela e curanto."
                ]
            },
            {
                "id": 10,
                "nome": "Peru",
                "bandeira": "data\\img\\Peru.bmp",
                "tips": [
                    "Localizado na costa oeste da América do Sul.",
                    "Possui uma grande diversidade climática, desde o deserto costeiro até a floresta amazônica e as montanhas dos Andes.",
                    "A topografia inclui montanhas, planaltos, vales férteis e uma extensa costa.",
                    "É conhecido por suas antigas civilizações, como os Incas, e por sua rica herança cultural.",
                    "Faz fronteira com Equador, Colômbia, Brasil, Bolívia e Chile.",
                    "Rico em recursos naturais como ouro, prata, cobre e petróleo.",
                    "É um dos principais produtores de prata e cobre do mundo.",
                    "A economia é diversificada, com setores como mineração, agricultura, pesca e turismo.",
                    "É um membro importante da Comunidade Andina e das Nações Unidas.",
                    "Desempenha um papel significativo na política e economia da América Latina.",
                    "Possui uma força militar moderna e bem treinada.",
                    "Exerce influência regional, especialmente nas questões de comércio e integração econômica.",
                    "Enfrenta desafios internos como desigualdade social, pobreza e questões ambientais.",
                    "Tem relações diplomáticas com muitos países e participa ativamente em fóruns regionais e internacionais.",
                    "Enfrenta conflitos internos relacionados a questões de terras indígenas e direitos sociais.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem o desenvolvimento econômico sustentável, a proteção ambiental e a promoção do turismo.",
                    "Conhecido por festivais como Inti Raymi e Semana Santa, além de estilos musicais como a marinera e a música andina.",
                    "A gastronomia é famosa mundialmente e inclui pratos como ceviche, lomo saltado, causa rellena e ají de gallina."
                ]
            },
            {
                "id": 11,
                "nome": "Colômbia",
                "bandeira": "data\\img\\Colombia.bmp",
                "tips": [
                    "Localizado no noroeste da América do Sul.",
                    "Possui uma grande diversidade geográfica, incluindo planícies costeiras, florestas tropicais, montanhas e planaltos.",
                    "A topografia inclui os Andes, a Amazônia e as planícies costeiras do Caribe e do Pacífico.",
                    "É conhecido por sua biodiversidade, sendo um dos países mais ricos em espécies do mundo, como a ave majestosa  Quetzal.",
                    "Faz fronteira com Venezuela, Brasil, Peru, Equador e Panamá.",
                    "Rico em recursos naturais como petróleo, gás natural, ouro e esmeraldas.",
                    "É um dos principais produtores de café e flores do mundo.",
                    "A economia é diversificada, com setores como agricultura, mineração, energia e turismo.",
                    "É um membro importante da Comunidade Andina e das Nações Unidas.",
                    "Desempenha um papel significativo na política e economia da América Latina.",
                    "Possui forças militares modernas e bem treinadas, envolvidas na luta contra o narcotráfico e grupos armados.",
                    "Exerce influência regional, especialmente nas questões de segurança e integração econômica.",
                    "Enfrenta desafios internos como o conflito armado interno, o narcotráfico e a desigualdade social.",
                    "Tem relações diplomáticas com muitos países e participa ativamente em fóruns regionais e internacionais.",
                    "Enfrenta conflitos internos relacionados a questões de terras, direitos humanos e segurança.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem a segurança interna, o desenvolvimento econômico sustentável e a proteção ambiental.",
                    "Possui festivais como o Carnaval de Barranquilla e o Festival de Vallenato e estilos musicais como cumbia, vallenato e salsa.",
                    "A gastronomia é diversificada e inclui pratos como bandeja paisa, arepas, sancocho e empanadas."
                ]
            },
            {
                "id": 12,
                "nome": "Estados Unidos",
                "bandeira": "data\\img\\EUA.bmp",
                "tips": [
                    "Localizado na América do Norte.",
                    "É o terceiro maior país do mundo em área territorial.",
                    "Possui uma grande diversidade geográfica, incluindo planícies, montanhas, desertos e costas.",
                    "Faz fronteira com Canadá, México e possui fronteiras marítimas com Rússia e Cuba, entre outros.",
                    "Rico em recursos naturais como petróleo, gás natural, minérios e terras aráveis.",
                    "É uma das maiores economias do mundo, com setores como tecnologia, indústria, agricultura e serviços.",
                    "É um dos membros permanentes do Conselho de Segurança das Nações Unidas.",
                    "Exerce influência global em política, economia, cultura e tecnologia.",
                    "Possui forças armadas poderosas, envolvidas em operações militares em todo o mundo.",
                    "Enfrenta desafios internos como questões raciais, desigualdade econômica e mudanças climáticas.",
                    "Tem uma forte presença diplomática em todo o mundo, com alianças e acordos internacionais, incluindo OTAN, TIAR, NAFTA e OMC.",
                    "Enfrenta conflitos internos relacionados a políticas domésticas e diferenças ideológicas.",
                    "É membro das Nações Unidas e contribui para operações de paz e segurança internacional.",
                    "Seus interesses nacionais incluem a segurança nacional, a prosperidade econômica e a defesa dos direitos humanos.",
                    "Conhecido por sua rica herança cultural, incluindo influências de diversas etnias, tradições regionais e expressões artísticas.",
                    "A gastronomia é diversificada e inclui pratos como hambúrgueres, pizza e uma variedade de comidas étnicas devido à imigração."
                ]
            },
            {
                "id": 13,
                "nome": "Canadá",
                "bandeira": "data\\img\\Canada.bmp",
                "tips": [
                    "Localizado na América do Norte, ao norte dos Estados Unidos.",
                    "É o segundo maior país do mundo em área territorial.",
                    "Possui uma geografia diversificada, incluindo vastas florestas, montanhas, pradarias e uma extensa costa marítima.",
                    "Faz fronteira com os Estados Unidos e possui uma das maiores fronteiras terrestres do mundo.",
                    "Rico em recursos naturais como petróleo, gás natural, minerais e vastas áreas de terras agrícolas.",
                    "É uma economia avançada, com setores como tecnologia, energia, mineração, agricultura e turismo.",
                    "É um dos membros fundadores da Organização das Nações Unidas (ONU).",
                    "Tem forte presença diplomática com laços estreitos com outros países através de organizações como a Comunidade das Nações, o G7 e o G20.",
                    "Desfruta de uma reputação de estabilidade política, paz e multiculturalismo.",
                    "Possui forças armadas modernas, com foco na defesa e na cooperação internacional em operações de paz.",
                    "Enfrenta desafios como a questão dos povos indígenas, mudanças climáticas e questões de soberania ártica.",
                    "Possui um sistema de saúde público universal e uma forte tradição de bem-estar social.",
                    "Tem uma rica herança cultural, influenciada por povos indígenas, colonizadores europeus e imigrantes de todo o mundo.",
                    "A culinária é diversificada e inclui pratos como poutine, tourtière, peixe, fritas e xarope de bordo, um símbolo nacional.",
                    "É conhecido por suas belezas naturais e parques nacionais, incluindo as Montanhas Rochosas e as Cataratas do Niágara."
                ]
            },
            {
                "id": 14,
                "nome": "México",
                "bandeira": "data\\img\\Mexico.bmp",
                "tips": [
                    "Localizado na América do Norte, ao sul dos Estados Unidos.",
                    "É o décimo quarto maior país do mundo em área territorial.",
                    "Possui uma geografia diversificada, incluindo planícies costeiras, montanhas, desertos e florestas tropicais.",
                    "Faz fronteira com os Estados Unidos, Guatemala e Belize, além de ter extensas costas no Oceano Pacífico e no Golfo do México.",
                    "Rico em recursos naturais como petróleo, prata, cobre e uma grande variedade de produtos agrícolas.",
                    "É uma economia em desenvolvimento, com setores como manufatura, turismo, agricultura e serviços.",
                    "É membro da ONU e participa ativamente de organizações regionais como o Mercosul e a Aliança do Pacífico.",
                    "Possui uma rica herança cultural, com influências indígenas, europeias e africanas.",
                    "É conhecido por sua arquitetura histórica, arte folclórica, festivais coloridos e rica gastronomia.",
                    "A culinária é reconhecida como Patrimônio Cultural Imaterial da Humanidade pela UNESCO com pratos como tacos, enchiladas, guacamole e chiles en nogada.",
                    "Enfrenta desafios como desigualdade econômica, pobreza, crime organizado e questões de imigração.",
                    "Possui uma força militar dedicada principalmente à segurança interna e à luta contra o tráfico de drogas.",
                    "Históricamente conhecida por civilizações como os Maias e os Astecas, preservados em sítios arqueológicos.",
                    "É um destino turístico popular, com praias deslumbrantes, sítios arqueológicos, cidades coloniais e uma vibrante vida noturna.",
                    "Possui uma importante indústria cinematográfica e é conhecido por seus talentosos diretores, atores e produções."
                ]
            },
            {
                "id": 15,
                "nome": "Cuba",
                "bandeira": "data\\img\\Cuba.bmp",
                "tips": [
                    "Localizada no Caribe, ao sul da Flórida.",
                    "É a maior ilha do Caribe e faz parte do arquipélago das Antilhas.",
                    "Possui uma geografia diversificada, incluindo planícies, montanhas e uma extensa costa.",
                    "Foi palco de influentes movimentos políticos e revolucionários, incluindo uma revolução liderada por Fidel Castro.",
                    "É conhecida por sua arquitetura colonial espanhola, praias paradisíacas e rica cultura.",
                    "Possui uma economia socialista, com setores como turismo, agricultura, saúde e educação controlados pelo estado.",
                    "Enfrenta desafios econômicos, incluindo o embargo comercial imposto pelos Estados Unidos.",
                    "É membro de organizações regionais como a CARICOM e a ALBA-TCP.",
                    "Possui uma forte tradição de arte e música, incluindo o famoso estilo de dança salsa.",
                    "A culinária é influenciada por diversas culturas e inclui pratos como ropa vieja, moros y cristianos, tostones e mojitos.",
                    "Tem um sistema de saúde reconhecido internacionalmente por sua qualidade e acessibilidade.",
                    "Possui uma alta taxa de alfabetização e educação gratuita para todos os cidadãos.",
                    "É conhecida por sua resistência cultural e sua política externa independente.",
                    "Apesar das restrições políticas e econômicas, mantém uma identidade única e um forte senso de nacionalismo.",
                    "É um destino turístico popular, especialmente para viajantes em busca de uma experiência autêntica do Caribe."
                ]
            },
            {
                "id": 16,
                "nome": "Jamaica",
                "bandeira": "data\\img\\Jamaica.bmp",
                "tips": [
                    "Localizada no Caribe, ao sul de Cuba.",
                    "Possui um clima tropical, com temperaturas quentes durante todo o ano e uma estação chuvosa entre maio e outubro.",
                    "Apresenta uma topografia diversificada, incluindo planícies costeiras, montanhas e florestas tropicais.",
                    "Tem uma área territorial de cerca de 11.000 km², tornando-se uma das maiores ilhas do Caribe.",
                    "Faz fronteira marítima com Cuba, ao norte, e com o Mar do Caribe, ao sul.",
                    "Rica em recursos naturais como minerais, especialmente bauxita.",
                    "A economia é impulsionada principalmente pelo turismo, agricultura (incluindo banana, cana-de-açúcar e café) e mineração.",
                    "Mantém relações internacionais estreitas, especialmente com países da Commonwealth e da região do Caribe.",
                    "Possui forças de defesa que incluem o Exército, a Marinha e a Força Aérea, focadas na segurança interna e na proteção das fronteiras marítimas.",
                    "É conhecida por seu estilo de vida descontraído, música reggae e cultura vibrante.",
                    "A culinária é picante e saborosa, com pratos tradicionais como jerk chicken, ackee e saltfish, e curry de cabra.",
                    "Enfrenta desafios sociais como crime, desemprego e pobreza, além de questões ambientais como a degradação dos recifes de coral.",
                    "É um destino turístico popular, com praias de areia branca, águas cristalinas e uma atmosfera descontraída e amigável.",
                    "A herança cultural, que inclui influências africanas, europeias e asiáticas."
                ]
            },
            {
                "id": 17,
                "nome": "China",
                "bandeira": "data\\img\\China.bmp",
                "tips": [
                    "Localizada no leste da Ásia, sendo o terceiro maior país do mundo em área territorial.",
                    "Apresenta uma grande diversidade de climas, incluindo tropical no sul, temperado no norte e desértico no oeste.",
                    "Possui uma topografia variada, incluindo planícies no leste, montanhas no oeste e desertos no norte.",
                    "É o país mais populoso do mundo, com uma população de mais de 1,4 bilhão de pessoas.",
                    "Faz fronteira com 14 países, incluindo Rússia, Índia e Coreia do Norte.",
                    "Rica em recursos naturais como carvão, minério de ferro, petróleo e gás natural.",
                    "É uma das maiores economias do mundo, com setores como manufatura, tecnologia, agricultura e serviços.",
                    "Possui relações internacionais complexas, incluindo alianças estratégicas, acordos comerciais e disputas territoriais.",
                    "Possui forças armadas modernas, com um grande foco na defesa e na projeção de poder regional.",
                    "Exerce influência global em política, economia, cultura e tecnologia.",
                    "Enfrenta desafios como poluição, desigualdade econômica, direitos humanos e tensões regionais.",
                    "É membro permanente do Conselho de Segurança das Nações Unidas.",
                    "Tem uma rica história e cultura, com contribuições significativas para arte, filosofia, medicina e gastronomia.",
                    "A culinária é variada e inclui pratos como dim sum, pato à Pequim, tofu e arroz frito.",
                    "Sua arquitetura tradicional, inclui a Grande Muralha, Torre de Xangai e o Centro Nacional de Artes Cênicas."
                ]
            },
            {
                "id": 18,
                "nome": "Índia",
                "bandeira": "data\\img\\India.bmp",
                "tips": [
                    "Localizada no sul da Ásia, sendo o sétimo maior país do mundo em área territorial.",
                    "Possui uma grande diversidade de climas, desde tropicais no sul até temperados no norte.",
                    "Apresenta uma topografia variada, incluindo planícies no norte, montanhas no noroeste e planaltos no centro.",
                    "É o segundo país mais populoso do mundo, com mais de 1,3 bilhão de habitantes.",
                    "Faz fronteira com Paquistão, China, Nepal, Butão, Bangladesh e Myanmar.",
                    "Rica em recursos naturais como carvão, minério de ferro, petróleo e gás natural.",
                    "É uma economia em crescimento, com setores como tecnologia, agricultura, manufatura e serviços.",
                    "Possui relações internacionais complexas, incluindo alianças estratégicas, acordos comerciais e disputas territoriais.",
                    "Possui forças armadas modernas, com foco na defesa e na segurança interna.",
                    "Exerce influência regional e global em política, economia e cultura.",
                    "Enfrenta desafios como pobreza, desigualdade econômica, poluição e tensões religiosas.",
                    "É membro das Nações Unidas e de várias organizações regionais e internacionais.",
                    "A culinária é diversificada e inclui pratos como curry, biryani, tandoori e samosa.",
                    "Conhecido por sua arquitetura tradicional, incluindo templos antigos e palácios  como o Taj Mahal e o Templo de Akshardham."
                ]
            },
            {
                "id": 19,
                "nome": "Coreia do Sul",
                "bandeira": "data\\img\\CoreiaSul.bmp",
                "tips": [
                    "Localizada no leste da Ásia, na Península da Coreia.",
                    "Possui um clima temperado, com verões quentes e úmidos e invernos frios e secos.",
                    "Apresenta uma topografia montanhosa, com cerca de 70% de seu território coberto por montanhas.",
                    "Faz fronteira com a Coreia do Norte, separada pela Zona Desmilitarizada.",
                    "Rica em recursos naturais como minerais, terras aráveis e energia hidrelétrica.",
                    "É uma das maiores economias do mundo, com foco em tecnologia, automóveis, eletrônicos, manufatura e turismo.",
                    "Possui relações internacionais complexas, incluindo alianças estratégicas, acordos comerciais e tensões históricas.",
                    "Possui forças armadas modernas, focadas principalmente na defesa contra a ameaça da Coreia do Norte.",
                    "Exerce influência regional e global em política, economia e cultura.",
                    "Enfrenta desafios como a tensão com a Coreia do Norte, questões de segurança regional e desigualdade de gênero.",
                    "É um dos principais membros da ONU e de várias organizações regionais e internacionais.",
                    "Tem uma rica história e cultura, influenciada por tradições confucionistas, budistas e xamânicas.",
                    "Contribuiu significativamente para a arte asiática, com obras de arte em cerâmica, pintura, escultura e arquitetura.",
                    "A música coreana abrange uma ampla gama de gêneros, incluindo trot, música clássica e folk.",
                    "A culinária é conhecida por pratos como kimchi, bulgogi, bibimbap e kimchi jjigae."
                ]
            },
            {
                "id": 20,
                "nome": "Coreia do Norte",
                "bandeira": "data\\img\\CoreiaNorte.bmp",
                "tips": [
                    "Localizada no leste da Ásia, na Península da Coreia.",
                    "Possui um clima continental, com verões quentes e invernos frios e secos.",
                    "Apresenta uma topografia montanhosa, com cerca de 80% de seu território coberto por montanhas.",
                    "Faz fronteira com a Coreia do Sul, separada pela Zona Desmilitarizada.",
                    "Rica em recursos naturais como minerais, carvão, magnésio e uma variedade de produtos agrícolas.",
                    "Possui uma economia centralizada, com foco na indústria pesada, agricultura e mineração.",
                    "Possui relações internacionais limitadas, mantendo-se isolada da comunidade internacional.",
                    "Possui forças armadas bem equipadas, focadas principalmente na defesa do regime e na manutenção do controle interno.",
                    "Exerce controle rígido sobre a sociedade, com um governo autoritário e um culto de personalidade em torno da dinastia Kim.",
                    "Enfrenta desafios como a escassez de alimentos, pobreza generalizada e violações dos direitos humanos.",
                    "É membro da ONU, embora tenha sido alvo de sanções devido a seu programa nuclear e direitos humanos.",
                    "Tem uma história e cultura marcadas por ideologias políticas, como o Juche e o culto à personalidade dos líderes.",
                    "A arte é usada para promover a ideologia do regime, com obras que glorificam os líderes e o regime.",
                    "A música é usada como uma ferramenta de propaganda, com canções que exaltam o país e seus líderes.",
                    "A literatura é fortemente controlada pelo governo e serve para promover a ideologia estatal.",
                    "A culinária é simples e baseada em alimentos locais, como arroz, vegetais, peixe e carne de porco.",
                    "Apesar do isolamento, mantém uma identidade cultural distinta, com festivais, danças e tradições únicas."
                ]
            },
            {
                "id": 21,
                "nome": "Alemanha",
                "bandeira": "data\\img\\Alemanha.bmp",
                "tips": [
                    "Localizada na Europa Central, fazendo fronteira com nove países, incluindo França, Áustria e Polônia.",
                    "Possui um clima temperado, com verões amenos e invernos frios.",
                    "Apresenta uma geografia diversificada, com planícies no norte, montanhas no sul e florestas no centro.",
                    "É o país mais populoso da União Europeia, com uma população de mais de 83 milhões de habitantes.",
                    "Rica em recursos naturais como carvão, gás natural, minério de ferro e uma agricultura diversificada.",
                    "É uma das maiores economias do mundo, com um forte foco em manufatura, tecnologia, automóveis e serviços.",
                    "Possui relações internacionais fortes, como membro da União Europeia e da OTAN.",
                    "Possui forças armadas modernas, focadas na defesa e em operações de paz internacionais.",
                    "É conhecida por sua estabilidade política, economia robusta e forte ênfase em educação e inovação.",
                    "Enfrenta desafios como a imigração, mudanças climáticas e envelhecimento da população.",
                    "É um líder global em questões como sustentabilidade, energias renováveis e direitos humanos.",
                    "Lar de compositores renomados como Beethoven, Bach e Brahms, que revolucionaram a música clássica.",
                    "Contribuiu para a filosofia com pensadores como Kant, Hegel e Nietzsche.",
                    "A culinária é conhecida por pratos como salsichas, pretzels, schnitzel, batata e cerveja.",
                    "É famosa por seus festivais culturais, como o Oktoberfest, e seus eventos esportivos, como a Copa do Mundo de Futebol."
                ]
            },
            {
                "id": 22,
                "nome": "França",
                "bandeira": "data\\img\\Franca.bmp",
                "tips": [
                    "Localizada no oeste da Europa, fazendo fronteira com nove países, incluindo Alemanha, Espanha e Itália.",
                    "Possui um clima diversificado, com regiões costeiras mediterrâneas, montanhas alpinas e planícies no norte.",
                    "Apresenta uma geografia variada, com cadeias montanhosas, rios importantes como o Sena e a Loire, e uma costa deslumbrante.",
                    "É o país mais visitado do mundo, com sua capital Paris sendo um dos principais destinos turísticos globais.",
                    "Rica em recursos naturais como agricultura, vinho, energia nuclear e turismo.",
                    "É uma das maiores economias do mundo, com destaque para indústrias como moda, perfumaria, automóveis, tecnologia e turismo.",
                    "Possui relações internacionais fortes, como membro da União Europeia, da OTAN e do Conselho de Segurança da ONU.",
                    "Possui forças armadas modernas, focadas na defesa e na segurança interna, além de participar de operações de paz internacionais.",
                    "É conhecida por sua rica cultura, que inclui arte, música, moda, gastronomia e filosofia.",
                    "Enfrenta desafios como imigração, desemprego, integração de comunidades étnicas e mudanças climáticas.",
                    "É um centro global de arte e cultura, com museus de renome mundial, galerias de arte e festivais culturais.",
                    "Tem uma rica história e cultura, com contribuições significativas para música, filosofia, ciência, literatura e arte.",
                    "Lar de compositores como Claude Debussy e Hector Berlioz, influentes na música clássica e impressionista.",
                    "Contribuiu para a filosofia com pensadores como René Descartes, Voltaire e Jean-Paul Sartre.",
                    "Foi berço de cientistas renomados como Marie Curie e Louis Pasteur, que fizeram avanços significativos em química e medicina.",
                    "Literatura inclui obras de Victor Hugo, Marcel Proust e Albert Camus.",
                    "A culinária é considerada uma das melhores do mundo, com pratos como croissants, queijos, vinhos, escargots e ratatouille.",
                    "É famosa por sua arquitetura icônica, incluindo a Torre Eiffel, o Louvre, a Catedral de Notre-Dame e o Palácio de Versalhes.",
                    "Possui uma história fascinante, que inclui períodos como a Revolução Francesa, o Império Napoleônico e as duas guerras mundiais.",
                    "É um líder global em moda, design, gastronomia, arte e literatura, influenciando a cultura global há séculos."
                ]
            },
            {
                "id": 23,
                "nome": "Reino Unido",
                "bandeira": "data\\img\\ReinoUnido.bmp",
                "tips": [
                    "Localizado na Europa Ocidental, compreendendo a Inglaterra, Escócia, País de Gales e Irlanda do Norte.",
                    "Possui um clima temperado marítimo, com verões frescos e invernos amenos.",
                    "Geografia variada, incluindo colinas onduladas, montanhas e costas acidentadas.",
                    "É uma ilha com fronteira terrestre apenas com a Irlanda, sendo separada da Europa continental pelo Canal da Mancha.",
                    "Rico em recursos naturais como carvão, petróleo e gás natural, além de uma agricultura diversificada.",
                    "Possui uma das maiores economias do mundo, com setores fortes em serviços financeiros, manufatura, tecnologia e comércio internacional.",
                    "Relações internacionais fortes, como membro permanente do Conselho de Segurança da ONU e da OTAN.",
                    "Possui forças armadas modernas, com capacidade nuclear e envolvimento em operações de paz e segurança global.",
                    "Historicamente, exerceu grande influência global através do seu império colonial.",
                    "Enfrenta desafios como o Brexit, a coesão interna entre seus países constituintes e questões de imigração.",
                    "É membro do G7, G20 e outras organizações internacionais importantes.",
                    "Enfrenta conflitos internos relacionados à independência da Escócia e à questão da fronteira irlandesa.",
                    "Tem uma longa tradição diplomática e de poder brando, influenciando culturas e políticas ao redor do mundo.",
                    "A culinária é conhecida por pratos tradicionais como fish and chips, roast beef e chá da tarde."
                ]
            },
            {
                "id": 24,
                "nome": "Itália",
                "bandeira": "data\\img\\Italia.bmp",
                "tips": [
                    "Localizada no sul da Europa, na Península Itálica, com fronteiras com França, Suíça, Áustria e Eslovênia.",
                    "Possui um clima mediterrâneo, com verões quentes e secos e invernos suaves e úmidos.",
                    "Geografia diversificada, com montanhas como os Alpes e os Apeninos, planícies férteis e uma longa costa mediterrânea.",
                    "Inclui duas grandes ilhas, Sicília e Sardenha, além de várias ilhas menores.",
                    "Rica em recursos naturais como mármore, granito e uma agricultura produtiva que inclui vinho, azeite de oliva e frutas.",
                    "Possui uma das maiores economias da Europa, com setores fortes em manufatura, design, moda, automóveis e turismo.",
                    "Relações internacionais fortes, como membro da União Europeia, da OTAN e do G7.",
                    "Possui forças armadas modernas, focadas em defesa e operações de paz internacionais.",
                    "Historicamente influente como o coração do Império Romano e um centro de renascimento cultural e científico durante a Renascença.",
                    "Enfrenta desafios como dívida pública elevada, crescimento econômico lento e questões de imigração.",
                    "É membro ativo da ONU e participa de várias missões de paz e segurança global.",
                    "Enfrenta conflitos internos relacionados a divisões econômicas entre o norte industrializado e o sul mais agrícola.",
                    "Tem um papel significativo na política, sendo uma voz importante na União Europeia.",
                    "A culinária é mundialmente famosa, com pratos como pizza, pasta, risoto e gelato."
                ]
            },
            {
                "id": 25,
                "nome": "Espanha",
                "bandeira": "data\\img\\Espanha.bmp",
                "tips": [
                    "Localizada no sudoeste da Europa, na Península Ibérica, fazendo fronteira com França, Portugal e Andorra.",
                    "Possui um clima variado, com clima mediterrâneo na maior parte do país, clima oceânico no norte e clima semiárido no sudeste.",
                    "Geografia diversificada, com cadeias montanhosas como os Pireneus e a Sierra Nevada, planícies centrais e uma extensa costa.",
                    "Inclui ilhas nas Baleares no Mediterrâneo e nas Canárias no Atlântico, além de cidades autônomas na África.",
                    "Rica em recursos naturais como carvão, urânio, zinco e uma agricultura produtiva, especialmente azeite de oliva e vinho.",
                    "Possui uma das maiores economias da Europa, com setores fortes em turismo, manufatura, agricultura e serviços.",
                    "Relações internacionais fortes, como membro da União Europeia, da OTAN e da ONU.",
                    "Possui forças armadas modernas, focadas em defesa nacional e missões internacionais de paz.",
                    "Tem uma história influente, com um vasto império colonial e um papel significativo na exploração e colonização das Américas.",
                    "Enfrenta desafios como a questão da independência da Catalunha, imigração e crescimento econômico.",
                    "É membro ativo de organizações internacionais como o G20, a ONU e a União Europeia.",
                    "Enfrenta conflitos internos relacionados à independência de regiões autônomas como Catalunha e País Basco.",
                    "Tem um papel importante na política e economia europeia, sendo um dos países fundadores da União Europeia.",
                    "A culinária é famosa por pratos como paella, tapas, jamón ibérico e tortilla espanhola."
                ]
            },
            {
                "id": 26,
                "nome": "Austrália",
                "bandeira": "data\\img\\Australia.bmp",
                "tips": [
                    "Localizada no hemisfério sul, compreendendo o continente australiano, a ilha da Tasmânia e várias ilhas menores.",
                    "Possui um clima variado, com clima tropical no norte, clima desértico no centro e clima temperado no sudeste e sudoeste.",
                    "Geografia diversificada, incluindo vastos desertos, florestas tropicais, montanhas e uma longa costa com praias famosas.",
                    "É o sexto maior país do mundo em área, com uma população concentrada principalmente nas regiões costeiras.",
                    "Rica em recursos naturais como carvão, ferro, ouro e gás natural, além de uma agricultura produtiva.",
                    "Possui uma das maiores economias da Ásia-Pacífico, com setores fortes em mineração, agricultura, serviços e turismo.",
                    "Relações internacionais fortes, como membro da ONU, da Commonwealth, da APEC e da ANZUS.",
                    "Possui forças armadas modernas, com foco na defesa nacional e na segurança regional.",
                    "Tem uma história marcada pela colonização britânica, com uma rica herança cultural indígena.",
                    "Enfrenta desafios como mudanças climáticas, gestão de recursos hídricos e questões de imigração.",
                    "É membro ativo de organizações internacionais e participa de missões de paz e ajuda humanitária.",
                    "Enfrenta conflitos relacionados a questões indígenas e políticas de imigração.",
                    "Tem um papel significativo na política e economia da região Ásia-Pacífico.",
                    "A culinária é conhecida por pratos como carne de canguru, pavlova, vegemite e frutos do mar frescos."
                ]
            },
            {
                "id": 27,
                "nome": "Nova Zelândia",
                "bandeira": "data\\img\\NovaZelandia.bmp",
                "tips": [
                    "Localizada no sudoeste do Pacífico, composta por duas ilhas principais, a Ilha Norte e a Ilha Sul, e várias ilhas menores.",
                    "Possui um clima temperado marítimo, com variações regionais significativas devido à geografia diversa.",
                    "Geografia diversificada, incluindo montanhas, florestas, lagos, praias e vulcões ativos.",
                    "Conhecida por suas paisagens naturais deslumbrantes, frequentemente utilizadas como locações para filmes.",
                    "Rica em recursos naturais como gás natural, carvão, madeira e uma agricultura altamente produtiva.",
                    "Possui uma economia diversificada, com setores fortes em agricultura, turismo, manufatura e serviços.",
                    "Relações internacionais fortes, como membro da ONU, da Commonwealth, da APEC e de várias alianças comerciais regionais.",
                    "Possui forças armadas modernas, com foco na defesa nacional e na participação em missões de paz internacionais.",
                    "Historicamente influenciada pela colonização britânica, com uma rica herança cultural maori.",
                    "Enfrenta desafios como a proteção ambiental, mudanças climáticas e a gestão de recursos naturais.",
                    "É membro ativo de organizações internacionais, com um papel significativo em questões ambientais e de paz.",
                    "Enfrenta conflitos relacionados a questões indígenas e direitos dos povos maori.",
                    "Tem uma política externa focada na cooperação regional e na manutenção da paz e segurança global.",
                    "A culinária é conhecida por pratos como carne de cordeiro, peixe e batata doce (kumara)."
                ]
            }
        ]
        self.paises_aleatorios = self.imagens

    def _atualizar_pais(self, cols):
        self.cols = cols
        self.y = 40
        self.x = self.config.janela_largura // 2
        self.paises_aleatorios = random.sample(self.imagens, cols)
        pais = random.choice(self.paises_aleatorios)
        self.pais_nome = pais["nome"]
        self.mostrar_pais = Botoes(self, self.pais_nome,self.x ,self.y)
        self.mostrar_pais.draw_botao()


import os
import sys
from flask import Flask, render_template, abort, url_for

# --- CONFIGURAÇÃO PARA EXECUTÁVEL (PyInstaller) ---
def resource_path(relative_path):
    """ 
    Obtém o caminho absoluto para os arquivos. 
    Necessário porque o PyInstaller extrai os arquivos em uma pasta temporária (_MEIPASS).
    """
    try:
        # Caminho da pasta temporária do PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Caminho do ambiente de desenvolvimento normal
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Inicializa o Flask apontando corretamente para as pastas de Front-end
app = Flask(__name__, 
            template_folder=resource_path("templates"),
            static_folder=resource_path("static"))

# --- BANCO DE DADOS COMPLETO (35 ITENS) ---
db_hardware = {
    # PLACAS DE VÍDEO (GPUs)
    "rtx-3060": {
        "nome": "NVIDIA GeForce RTX 3060",
        "categoria": "Placas de Vídeo",
        "img": "rtx3060.jpg",
        "definicao": "A RTX 3060 é a porta de entrada para o Ray Tracing de alta performance. Com 12GB de VRAM, ela é capaz de renderizar cenas complexas e iluminação global realista com auxílio de IA.",
        "specs": ["Memória: 12GB GDDR6", "Cores: 3584 CUDA", "Clock: 1.32 GHz", "TDP: 170W"]
    },
    "rtx-4090": {
        "nome": "NVIDIA GeForce RTX 4090",
        "categoria": "Placas de Vídeo",
        "img": "rtx4090.jpg",
        "definicao": "A GPU mais potente do mundo atual. Utiliza a arquitetura Ada Lovelace e o DLSS 3 para gerar quadros inteiros por IA, permitindo 4K nativo no ultra.",
        "specs": ["Memória: 24GB GDDR6X", "Cores: 16384 CUDA", "Clock: 2.23 GHz", "TDP: 450W"]
    },
    "rx-6700": {
        "nome": "AMD Radeon RX 6700 XT",
        "categoria": "Placas de Vídeo",
        "img": "rx6700.jpg",
        "definicao": "Focada em 1440p, utiliza o Infinity Cache de 96MB para reduzir latências e entregar uma fluidez excepcional em jogos de mundo aberto.",
        "specs": ["Memória: 12GB GDDR6", "Cache: 96MB Infinity", "Interface: PCIe 4.0", "TDP: 230W"]
    },
    "gtx-1650": {
        "nome": "NVIDIA GeForce GTX 1650",
        "categoria": "Placas de Vídeo",
        "img": "gtx1650.jpg",
        "definicao": "A queridinha dos setups de entrada. Extremamente eficiente, muitas vezes dispensa conectores de energia da fonte, sendo ideal para eSports.",
        "specs": ["Memória: 4GB GDDR6", "Cores: 896 CUDA", "Arquitetura: Turing", "TDP: 75W"]
    },
    "rx-7900": {
        "nome": "AMD Radeon RX 7900 XTX",
        "categoria": "Placas de Vídeo",
        "img": "rx7900.jpg",
        "definicao": "A primeira GPU baseada em design de chiplets. Oferece largura de banda massiva e suporte a DisplayPort 2.1 para monitores de próxima geração.",
        "specs": ["Memória: 24GB GDDR6", "Interface: 384-bit", "Arquitetura: RDNA 3", "TDP: 355W"]
    },

    # PROCESSADORES (CPUs)
    "i5-13600k": {
        "nome": "Intel Core i5-13600K",
        "categoria": "Processadores",
        "img": "i5.jpg",
        "definicao": "Um processador híbrido que combina núcleos de performance e eficiência, sendo o equilíbrio perfeito para streamers e gamers.",
        "specs": ["Núcleos: 14 (6P+8E)", "Threads: 20", "Clock: 5.1 GHz", "Socket: LGA1700"]
    },
    "r7-7800x3d": {
        "nome": "AMD Ryzen 7 7800X3D",
        "categoria": "Processadores",
        "img": "r7.jpg",
        "definicao": "Considerado o melhor processador para jogos do mundo graças à tecnologia 3D V-Cache, que empilha memória cache para eliminar gargalos.",
        "specs": ["Núcleos: 8", "Threads: 16", "L3 Cache: 96MB", "Socket: AM5"]
    },
    "i9-14900k": {
        "nome": "Intel Core i9-14900K",
        "categoria": "Processadores",
        "img": "i9.jpg",
        "definicao": "Poder bruto absoluto. Capaz de atingir 6.0 GHz, é voltado para profissionais de renderização pesada e entusiastas de overclock.",
        "specs": ["Núcleos: 24 (8P+16E)", "Threads: 32", "Clock: 6.0 GHz", "Cache: 36MB L3"]
    },
    "r5-5600": {
        "nome": "AMD Ryzen 5 5600",
        "categoria": "Processadores",
        "img": "r5.jpg",
        "definicao": "O rei do custo-benefício. Entrega alta performance na plataforma AM4 com um consumo de energia e dissipação de calor muito baixos.",
        "specs": ["Núcleos: 6", "Threads: 12", "Clock: 3.5GHz - 4.4GHz", "Socket: AM4"]
    },
    "i3-12100": {
        "nome": "Intel Core i3-12100",
        "categoria": "Processadores",
        "img": "i3.jpg",
        "definicao": "O quad-core mais eficiente da geração Alder Lake, superando muitos processadores de 8 núcleos de gerações passadas em tarefas únicas.",
        "specs": ["Núcleos: 4", "Threads: 8", "Clock: 4.3 GHz", "Socket: LGA1700"]
    },

    # PLACAS-MÃE (Motherboards)
    "z790-e": {
        "nome": "ASUS ROG Strix Z790-E",
        "categoria": "Placas-Mãe",
        "img": "z790.jpg",
        "definicao": "Placa-mãe de elite para entusiastas. Possui VRMs robustos para overclock extremo e suporte nativo a memórias DDR5 ultra-rápidas.",
        "specs": ["Chipset: Z790", "Fases: 18+1", "Rede: Wi-Fi 6E", "Suporte: DDR5"]
    },
    "b550m-pro": {
        "nome": "MSI B550M Pro-VDH",
        "categoria": "Placas-Mãe",
        "img": "b550.jpg",
        "definicao": "A escolha sólida para a plataforma AM4. Oferece suporte a PCIe 4.0 e dissipadores de calor eficientes para o uso diário intenso.",
        "specs": ["Chipset: B550", "Formato: Micro-ATX", "Slots: 2x M.2", "Suporte: DDR4"]
    },
    "x670e-aorus": {
        "nome": "Gigabyte X670E Aorus Master",
        "categoria": "Placas-Mãe",
        "img": "x670.jpg",
        "definicao": "Topo de linha para o socket AM5. Preparada para o futuro com barramento PCIe 5.0 total para placas de vídeo e SSDs.",
        "specs": ["Chipset: X670E", "PCIe: Gen 5.0", "USB: 4.0 Support", "Suporte: DDR5"]
    },
    "b660-steel": {
        "nome": "ASRock B660 Steel Legend",
        "categoria": "Placas-Mãe",
        "img": "b660.jpg",
        "definicao": "Construção premium com dissipadores em aço. Ideal para processadores Intel Core de 12ª e 13ª geração focado em estabilidade.",
        "specs": ["Chipset: B660", "Design: Steel Legend", "Iluminação: RGB Sync", "Suporte: DDR4"]
    },
    "b650-plus": {
        "nome": "ASUS TUF Gaming B650-Plus",
        "categoria": "Placas-Mãe",
        "img": "b650.jpg",
        "definicao": "Durabilidade de classe militar. Feita para aguentar temperaturas altas e uso contínuo em workstations e setups gamer AM5.",
        "specs": ["Chipset: B650", "Padrão: TUF Military", "Rede: 2.5Gb Ethernet", "Suporte: DDR5"]
    },

    # MEMÓRIA RAM
    "ram-corsair": {
        "nome": "Corsair Vengeance 16GB",
        "categoria": "Memória RAM",
        "img": "ram_corsair.jpg",
        "definicao": "Memória RAM de alta velocidade DDR5. Essencial para alimentar processadores modernos com dados em tempo real.",
        "specs": ["Capacidade: 16GB (2x8)", "Velocidade: 5200MHz", "Tipo: DDR5", "Perfil: XMP 3.0"]
    },
    "ram-gskill": {
        "nome": "G.Skill Trident Z5 32GB",
        "categoria": "Memória RAM",
        "img": "ram_gskill.jpg",
        "definicao": "Módulos selecionados para baixa latência. Além do visual RGB impecável, entrega estabilidade em frequências extremas.",
        "specs": ["Capacidade: 32GB (2x16)", "Velocidade: 6000MHz", "Tipo: DDR5", "Latência: CL30"]
    },
    "ram-kingston": {
        "nome": "Kingston Fury Beast 8GB",
        "categoria": "Memória RAM",
        "img": "ram_kingston.jpg",
        "definicao": "A memória mais vendida e confiável do mundo. Com dissipador de baixo perfil, é compatível com quase todos os air coolers.",
        "specs": ["Capacidade: 8GB", "Velocidade: 3200MHz", "Tipo: DDR4", "Latência: CL16"]
    },
    "ram-tforce": {
        "nome": "TeamGroup T-Force Delta",
        "categoria": "Memória RAM",
        "img": "ram_tforce.jpg",
        "definicao": "Design agressivo e iluminação RGB de 120 graus. Possui dissipador em alumínio de alta densidade para controle térmico.",
        "specs": ["Capacidade: 16GB (2x8)", "Velocidade: 3600MHz", "Tipo: DDR4", "RGB: Full Frame"]
    },
    "ram-crucial": {
        "nome": "Crucial Pro 32GB",
        "categoria": "Memória RAM",
        "img": "ram_crucial.jpg",
        "definicao": "Focada em estabilidade corporativa e profissional. Sem luzes, foca 100% no desempenho bruto e integridade de dados.",
        "specs": ["Capacidade: 32GB (2x16)", "Velocidade: 3200MHz", "Tipo: DDR4", "Série: Pro Performance"]
    },

    # ARMAZENAMENTO (SSD/HD)
    "ssd-samsung": {
        "nome": "Samsung 980 Pro 1TB",
        "categoria": "Armazenamento",
        "img": "ssd_samsung.jpg",
        "definicao": "O padrão ouro dos SSDs NVMe Gen 4. Carrega jogos e sistemas operacionais em frações de segundos.",
        "specs": ["Leitura: 7000 MB/s", "Gravação: 5000 MB/s", "Tipo: NVMe Gen4", "Cache: 1GB LPDDR4"]
    },
    "ssd-kingston": {
        "nome": "Kingston NV2 2TB",
        "categoria": "Armazenamento",
        "img": "ssd_kingston.jpg",
        "definicao": "SSD NVMe de alta capacidade com custo acessível. Ideal para armazenar bibliotecas imensas de jogos AAA.",
        "specs": ["Capacidade: 2TB", "Leitura: 3500 MB/s", "Interface: M.2 NVMe Gen4", "MTBF: 1.5 Milhões h"]
    },
    "hd-wd": {
        "nome": "WD Blue 1TB HDD",
        "categoria": "Armazenamento",
        "img": "hd_wd.jpg",
        "definicao": "Disco rígido mecânico clássico. Perfeito para backup de fotos e vídeos onde a velocidade não é prioridade.",
        "specs": ["Capacidade: 1TB", "Rotação: 7200 RPM", "Cache: 64MB", "SATA: III"]
    },
    "hd-seagate": {
        "nome": "Seagate Barracuda 4TB",
        "categoria": "Armazenamento",
        "img": "hd_seagate.jpg",
        "definicao": "Armazenamento massivo para coleções digitais. Utiliza gravação magnética confiável para longa duração.",
        "specs": ["Capacidade: 4TB", "Cache: 256MB", "Interface: SATA 6Gb/s", "Formato: 3.5 pol"]
    },
    "ssd-crucial": {
        "nome": "Crucial MX500 500GB",
        "categoria": "Armazenamento",
        "img": "ssd_crucial.jpg",
        "definicao": "Melhor upgrade para notebooks antigos. O formato SATA substitui HDs velhos tornando o PC até 10x mais rápido.",
        "specs": ["Leitura: 560 MB/s", "Gravação: 510 MB/s", "Tipo: SATA III 2.5", "Tecnologia: 3D NAND"]
    },

    # FONTES (PSU)
    "psu-corsair": {
        "nome": "Corsair RM850x",
        "categoria": "Fontes",
        "img": "psu_corsair.jpg",
        "definicao": "Fonte totalmente modular com capacitores japoneses. Entrega energia limpa e silenciosa para GPUs potentes.",
        "specs": ["Potência: 850W", "Selo: 80 Plus Gold", "Modular: Sim", "Ventoinha: Magnetic Levitation"]
    },
    "psu-evga": {
        "nome": "EVGA 600 W1",
        "categoria": "Fontes",
        "img": "psu_evga.jpg",
        "definicao": "Opção de entrada confiável. Possui proteções vitais contra sobretensões, protegendo seu investimento.",
        "specs": ["Potência: 600W", "Selo: 80 Plus White", "PFC: Ativo", "Trilho: +12V Single"]
    },
    "psu-seasonic": {
        "nome": "Seasonic Focus GX-750",
        "categoria": "Fontes",
        "img": "psu_seasonic.jpg",
        "definicao": "Referência mundial em estabilidade. A Seasonic é a fabricante que define os padrões de qualidade elétrica.",
        "specs": ["Potência: 750W", "Selo: 80 Plus Gold", "Modular: Total", "Controle: Hybrid Silent Fan"]
    },
    "psu-cm": {
        "nome": "Cooler Master MWE 650",
        "categoria": "Fontes",
        "img": "psu_cm.jpg",
        "definicao": "Fonte intermediária com tecnologia DC-to-DC, garantindo que as linhas de 3V e 5V sejam sempre estáveis.",
        "specs": ["Potência: 650W", "Selo: 80 Plus Bronze", "Circuito: DC-to-DC", "Ventoinha: HDB"]
    },
    "psu-msi": {
        "nome": "MSI MAG A850GL",
        "categoria": "Fontes",
        "img": "psu_msi.jpg",
        "definicao": "Fonte de última geração ATX 3.0. Já inclui o cabo 12VHPWR nativo para as placas RTX Série 40.",
        "specs": ["Potência: 850W", "Padrão: ATX 3.0", "PCIe: 5.0 Ready", "Selo: 80 Plus Gold"]
    },

    # MONITORES
    "mon-lg": {
        "nome": "LG UltraGear 27",
        "categoria": "Monitores",
        "img": "mon_lg.jpg",
        "definicao": "Monitor IPS focado em velocidade. O tempo de resposta de 1ms elimina o efeito fantasma em jogos rápidos.",
        "specs": ["Tamanho: 27 pol", "Freq: 144Hz", "Painel: IPS", "Resposta: 1ms GtG"]
    },
    "mon-samsung": {
        "nome": "Samsung Odyssey G5",
        "categoria": "Monitores",
        "img": "mon_samsung.jpg",
        "definicao": "Curvatura 1000R extrema para imersão total. A resolução QHD oferece 1.7x mais pixels que o Full HD.",
        "specs": ["Tamanho: 32 pol", "Freq: 144Hz", "Resolução: 2K (QHD)", "Curvatura: 1000R"]
    },
    "mon-alien": {
        "nome": "Dell Alienware 34",
        "categoria": "Monitores",
        "img": "mon_alien.jpg",
        "definicao": "O ápice tecnológico com painel QD-OLED. Contraste infinito e cores que superam qualquer monitor comum.",
        "specs": ["Tamanho: 34 pol UW", "Freq: 165Hz", "Painel: QD-OLED", "Resposta: 0.1ms"]
    },
    "mon-asus": {
        "nome": "ASUS TUF VG249Q",
        "categoria": "Monitores",
        "img": "mon_asus.jpg",
        "definicao": "Monitor favorito para eSports. Tamanho de 24 polegadas ideal para manter todo o campo de visão focado.",
        "specs": ["Tamanho: 23.8 pol", "Freq: 144Hz", "Ajuste: Altura e Pivot", "Filtro: Blue Light"]
    },
    "mon-aoc": {
        "nome": "AOC Hero 27",
        "categoria": "Monitores",
        "img": "mon_aoc.jpg",
        "definicao": "Melhor custo-benefício em 27 polegadas. Oferece fluidez e cores vibrantes para qualquer tipo de jogo.",
        "specs": ["Tamanho: 27 pol", "Freq: 144Hz", "Painel: IPS", "Tecnologia: G-Sync Comp."]
    },
}

# --- ESTRUTURA PARA A BARRA LATERAL ---
estrutura_categorias = {
    "Placas de Vídeo": ["rtx-3060", "rtx-4090", "rx-6700", "gtx-1650", "rx-7900"],
    "Processadores": ["i5-13600k", "r7-7800x3d", "i9-14900k", "r5-5600", "i3-12100"],
    "Placas-Mãe": ["z790-e", "b550m-pro", "x670e-aorus", "b660-steel", "b650-plus"],
    "Memória RAM": ["ram-corsair", "ram-gskill", "ram-kingston", "ram-tforce", "ram-crucial"],
    "Armazenamento": ["ssd-samsung", "ssd-kingston", "hd-wd", "hd-seagate", "ssd-crucial"],
    "Fontes": ["psu-corsair", "psu-evga", "psu-seasonic", "psu-cm", "psu-msi"],
    "Monitores": ["mon-lg", "mon-samsung", "mon-alien", "mon-asus", "mon-aoc"]
}

@app.route('/')
def home():
    return render_template('index.html', categorias=estrutura_categorias, db=db_hardware)

@app.route('/componente/<slug>')
def detalhe(slug):
    item = db_hardware.get(slug)
    if not item:
        abort(404)
    return render_template('detalhes.html', item=item)

if __name__ == '__main__':
    # Em produção/executável, o debug deve ser False
    app.run(debug=True)
#!/usr/bin/env python3
"""
Gerador de Proposta Comercial - Monarca Administradora de Condomínios
Gera um PDF profissional de 16 páginas usando WeasyPrint.
"""

import base64
import os
from weasyprint import HTML

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "versão-solidas.png")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "Proposta_Comercial_Monarca.pdf")

# Read and encode logo
with open(LOGO_PATH, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("utf-8")

LOGO_DATA_URI = f"data:image/png;base64,{logo_base64}"

# Color palette
PRIMARY_DARK = "#0e2a35"
SECONDARY = "#0090a8"
ACCENT_LIGHT = "#f9e8bd"
ACCENT = "#e0bf8c"
WHITE = "#ffffff"
LIGHT_GRAY = "#f5f5f5"


def build_css():
    return f"""

@page {{
    size: A4;
    margin: 0;
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: {PRIMARY_DARK};
    line-height: 1.6;
}}

.page {{
    width: 210mm;
    height: 297mm;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    padding: 0;
}}

.page:last-child {{
    page-break-after: auto;
}}

/* Dark pages */
.page-dark {{
    background: {PRIMARY_DARK};
    color: {WHITE};
}}

.page-light {{
    background: {WHITE};
    color: {PRIMARY_DARK};
}}

.page-gray {{
    background: {LIGHT_GRAY};
    color: {PRIMARY_DARK};
}}

/* Content containers */
.content {{
    padding: 60px 70px;
    height: 100%;
    position: relative;
}}

.content-centered {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}}

/* Typography */
h1 {{
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.2;
}}

h2 {{
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 16px;
    line-height: 1.3;
}}

h3 {{
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
}}

p {{
    font-size: 14px;
    line-height: 1.7;
    margin-bottom: 12px;
}}

.subtitle {{
    font-size: 16px;
    line-height: 1.6;
    opacity: 0.9;
    margin-bottom: 24px;
}}

/* Accent elements */
.accent-bar {{
    width: 60px;
    height: 4px;
    background: {SECONDARY};
    margin-bottom: 24px;
}}

.accent-bar-gold {{
    width: 60px;
    height: 4px;
    background: {ACCENT};
    margin-bottom: 24px;
}}

.accent-bar-white {{
    width: 60px;
    height: 4px;
    background: {WHITE};
    margin-bottom: 24px;
}}

/* Grid layouts */
.grid-2x3 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-top: 30px;
}}

.grid-3x2 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    margin-top: 30px;
}}

.grid-2x1 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-top: 30px;
}}

/* Cards */
.card {{
    background: {WHITE};
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}}

.card-dark {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 12px;
    padding: 24px;
}}

.card-teal {{
    background: {SECONDARY};
    color: {WHITE};
    border-radius: 12px;
    padding: 24px;
}}

.card-outlined {{
    border: 1px solid rgba(14,42,53,0.12);
    border-radius: 12px;
    padding: 24px;
    background: {WHITE};
}}

.card h3 {{
    color: {SECONDARY};
    margin-bottom: 8px;
}}

.card-dark h3 {{
    color: {ACCENT_LIGHT};
    margin-bottom: 8px;
}}

.card-teal h3 {{
    color: {WHITE};
}}

.card p, .card-dark p, .card-outlined p {{
    font-size: 13px;
    opacity: 0.85;
}}

/* Decorative shapes */
.circle-deco {{
    position: absolute;
    border-radius: 50%;
    opacity: 0.08;
}}

.corner-accent {{
    position: absolute;
    top: 0;
    right: 0;
    width: 200px;
    height: 200px;
    background: linear-gradient(135deg, {SECONDARY}, transparent);
    opacity: 0.15;
}}

/* Page number */
.page-number {{
    position: absolute;
    bottom: 30px;
    right: 70px;
    font-size: 11px;
    opacity: 0.5;
}}

.page-number-light {{
    color: {WHITE};
}}

/* Logo */
.logo {{
    width: 220px;
    margin-bottom: 40px;
}}

.logo-small {{
    width: 100px;
    position: absolute;
    top: 40px;
    left: 70px;
}}

/* Highlights */
.highlight-row {{
    display: flex;
    gap: 20px;
    margin-top: 30px;
    flex-wrap: wrap;
}}

.highlight-item {{
    background: rgba(0,144,168,0.08);
    border-left: 3px solid {SECONDARY};
    padding: 12px 18px;
    border-radius: 0 8px 8px 0;
    flex: 1;
    min-width: 150px;
}}

.highlight-item p {{
    font-size: 13px;
    font-weight: 600;
    color: {SECONDARY};
    margin: 0;
}}

/* Timeline */
.timeline {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 16px;
    margin-top: 30px;
}}

.timeline-item {{
    text-align: center;
    position: relative;
}}

.timeline-number {{
    width: 36px;
    height: 36px;
    background: {SECONDARY};
    color: {WHITE};
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
    margin: 0 auto 10px;
}}

.timeline-item p {{
    font-size: 12px;
    font-weight: 600;
}}

/* Features */
.feature-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-top: 24px;
}}

.feature-item {{
    background: rgba(0,144,168,0.06);
    border-radius: 10px;
    padding: 20px;
    text-align: center;
}}

.feature-item h3 {{
    color: {SECONDARY};
    font-size: 14px;
}}

/* Top bar decoration */
.top-bar {{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, {SECONDARY}, {ACCENT});
}}

/* Bottom decoration */
.bottom-deco {{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 80px;
    background: linear-gradient(0deg, rgba(14,42,53,0.03), transparent);
}}

/* CTA page */
.cta-box {{
    background: {SECONDARY};
    color: {WHITE};
    border-radius: 16px;
    padding: 40px;
    text-align: center;
    margin-top: 30px;
}}

.cta-box h2 {{
    color: {WHITE};
    margin-bottom: 16px;
}}

.contact-info {{
    margin-top: 30px;
    text-align: left;
}}

.contact-item {{
    display: flex;
    align-items: center;
    margin-bottom: 12px;
    font-size: 14px;
}}

/* Section tag */
.section-tag {{
    display: inline-block;
    background: rgba(0,144,168,0.1);
    color: {SECONDARY};
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 20px;
}}

.section-tag-light {{
    background: rgba(255,255,255,0.15);
    color: {WHITE};
}}

/* Geometric background */
.geo-bg {{
    position: absolute;
    top: -50px;
    right: -50px;
    width: 300px;
    height: 300px;
    border: 40px solid rgba(0,144,168,0.05);
    border-radius: 50%;
}}

.geo-bg-2 {{
    position: absolute;
    bottom: -80px;
    left: -80px;
    width: 250px;
    height: 250px;
    border: 30px solid rgba(224,191,140,0.08);
    border-radius: 50%;
}}
"""



def build_page1():
    """CAPA"""
    return f"""
    <div class="page page-dark">
        <div class="content content-centered">
            <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(ellipse at 30% 20%, rgba(0,144,168,0.15) 0%, transparent 60%);"></div>
            <div style="position:absolute;bottom:-100px;right:-100px;width:400px;height:400px;border:50px solid rgba(224,191,140,0.06);border-radius:50%;"></div>
            <div style="position:absolute;top:-60px;left:-60px;width:200px;height:200px;border:25px solid rgba(0,144,168,0.08);border-radius:50%;"></div>
            <img src="{LOGO_DATA_URI}" class="logo" alt="Monarca Logo" style="width:260px;margin-bottom:50px;position:relative;z-index:1;">
            <div style="position:relative;z-index:1;">
                <div style="width:80px;height:2px;background:{ACCENT};margin:0 auto 30px;"></div>
                <h1 style="font-size:28px;font-weight:300;letter-spacing:4px;color:{WHITE};margin-bottom:10px;">PROPOSTA COMERCIAL</h1>
                <p style="font-size:16px;color:{ACCENT_LIGHT};opacity:0.8;letter-spacing:2px;">2025</p>
            </div>
        </div>
    </div>
    """


def build_page2():
    """APRESENTACAO INSTITUCIONAL"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div class="geo-bg"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Apresenta\u00e7\u00e3o</span>
                <h1 style="font-size:30px;color:{PRIMARY_DARK};max-width:500px;">Gest\u00e3o condominial com m\u00e9todo, presen\u00e7a e clareza</h1>
                <div class="accent-bar"></div>
                <p style="font-size:15px;max-width:550px;color:#444;line-height:1.8;">
                    A Monarca Administradora estrutura a rotina do condom\u00ednio para que s\u00edndico, conselho e moradores tenham mais controle, transpar\u00eancia e seguran\u00e7a nas decis\u00f5es do dia a dia. Com uma atua\u00e7\u00e3o pr\u00f3xima e solu\u00e7\u00f5es digitais, a administra\u00e7\u00e3o se torna mais organizada, acess\u00edvel e preparada para atender as necessidades de cada condom\u00ednio.
                </p>
                <div class="highlight-row">
                    <div class="highlight-item">
                        <p>100% foco na rotina condominial</p>
                    </div>
                    <div class="highlight-item">
                        <p>+ processos organizados</p>
                    </div>
                    <div class="highlight-item">
                        <p>SC - Porto Belo, Itapema e Tijucas</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">02</div>
    </div>
    """


def build_page3():
    """SOBRE A MONARCA"""
    return f"""
    <div class="page page-dark">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(160deg, {PRIMARY_DARK} 0%, #0a1f28 100%);"></div>
        <div style="position:absolute;bottom:-80px;right:-80px;width:350px;height:350px;border:40px solid rgba(0,144,168,0.08);border-radius:50%;"></div>
        <div class="content" style="position:relative;z-index:1;padding-top:80px;">
            <span class="section-tag section-tag-light">Sobre n\u00f3s</span>
            <h1 style="color:{WHITE};font-size:30px;">Monarca, administra\u00e7\u00e3o pr\u00f3xima</h1>
            <div class="accent-bar-gold"></div>
            <p class="subtitle" style="color:rgba(255,255,255,0.8);max-width:520px;">
                Uma administradora preparada para transformar a rotina condominial em um processo mais simples, claro e bem acompanhado.
            </p>
            <div style="margin-top:40px;">
                <div class="card-dark" style="margin-bottom:20px;">
                    <h3>Atendimento personalizado</h3>
                    <p>Cada condom\u00ednio tem particularidades. Por isso, a gest\u00e3o \u00e9 conduzida com aten\u00e7\u00e3o \u00e0s necessidades espec\u00edficas.</p>
                </div>
                <div class="card-dark" style="margin-bottom:20px;">
                    <h3>Transpar\u00eancia administrativa</h3>
                    <p>Informa\u00e7\u00f5es, documentos, comunicados e movimenta\u00e7\u00f5es s\u00e3o organizados para facilitar o acompanhamento.</p>
                </div>
                <div class="card-dark">
                    <h3>Apoio ao s\u00edndico</h3>
                    <p>Suporte para decis\u00f5es, demandas recorrentes e organiza\u00e7\u00e3o das prioridades do condom\u00ednio.</p>
                </div>
            </div>
        </div>
        <div class="page-number page-number-light">03</div>
    </div>
    """



def build_page4():
    """PILARES DA GESTAO"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div class="geo-bg-2"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Pilares</span>
                <h2 style="color:{PRIMARY_DARK};">Controle, transpar\u00eancia e experi\u00eancia condominial</h2>
                <div class="accent-bar"></div>
                <p class="subtitle" style="color:#555;max-width:520px;">A gest\u00e3o eficiente nasce da combina\u00e7\u00e3o entre organiza\u00e7\u00e3o financeira, comunica\u00e7\u00e3o objetiva e acompanhamento constante das demandas.</p>
                <div class="grid-2x3">
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};">Controle financeiro</h3>
                        <p>Movimenta\u00e7\u00f5es, boletos e pagamentos acompanhados com clareza.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};">Comunica\u00e7\u00e3o objetiva</h3>
                        <p>Avisos e informa\u00e7\u00f5es importantes em canais organizados.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};">Presen\u00e7a na rotina</h3>
                        <p>Apoio constante para s\u00edndico, conselho e moradores.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};">Organiza\u00e7\u00e3o documental</h3>
                        <p>Atas, editais e documentos acess\u00edveis quando necess\u00e1rio.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};">Processos digitais</h3>
                        <p>Ferramentas que simplificam reservas, ocorr\u00eancias e comunicados.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};">Conviv\u00eancia facilitada</h3>
                        <p>Mais praticidade para melhorar a experi\u00eancia dos moradores.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">04</div>
    </div>
    """


def build_page5():
    """SOLUCOES"""
    return f"""
    <div class="page page-dark">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(135deg, {PRIMARY_DARK} 0%, #0a3040 50%, {PRIMARY_DARK} 100%);"></div>
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;height:500px;border:60px solid rgba(0,144,168,0.04);border-radius:50%;"></div>
        <div class="content content-centered" style="position:relative;z-index:1;">
            <span class="section-tag section-tag-light">Solu\u00e7\u00f5es</span>
            <h1 style="font-size:36px;color:{WHITE};margin-bottom:20px;">Solu\u00e7\u00f5es Monarca</h1>
            <div style="width:80px;height:3px;background:{ACCENT};margin:0 auto 30px;"></div>
            <p style="font-size:16px;color:rgba(255,255,255,0.85);max-width:480px;line-height:1.8;">
                Servi\u00e7os pensados para proteger a rotina administrativa, fortalecer a transpar\u00eancia e melhorar a experi\u00eancia de todos no condom\u00ednio.
            </p>
            <div style="margin-top:40px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:30px 40px;max-width:500px;">
                <p style="font-size:14px;color:rgba(255,255,255,0.7);line-height:1.8;">
                    Administra\u00e7\u00e3o eficiente e transparente para condom\u00ednios que buscam clareza, controle e suporte especializado.
                </p>
            </div>
        </div>
        <div class="page-number page-number-light">05</div>
    </div>
    """


def build_page6():
    """SERVICOS"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Servi\u00e7os</span>
                <h2 style="color:{PRIMARY_DARK};">O que a Monarca entrega ao seu condom\u00ednio</h2>
                <div class="accent-bar"></div>
                <div class="grid-2x3">
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Assessoria ao s\u00edndico</h3>
                        <p>Apoio para condu\u00e7\u00e3o das rotinas, organiza\u00e7\u00e3o de demandas e acompanhamento das prioridades.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Gest\u00e3o administrativa</h3>
                        <p>Estrutura\u00e7\u00e3o de processos, documentos, comunicados e informa\u00e7\u00f5es condominiais.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Gest\u00e3o financeira</h3>
                        <p>Controle de receitas, despesas, boletos, pagamentos e presta\u00e7\u00e3o de contas.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Gest\u00e3o cont\u00e1bil</h3>
                        <p>Organiza\u00e7\u00e3o das informa\u00e7\u00f5es cont\u00e1beis para uma administra\u00e7\u00e3o mais regular e transparente.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Manuten\u00e7\u00e3o predial</h3>
                        <p>Registro e acompanhamento das atividades de conserva\u00e7\u00e3o e manuten\u00e7\u00e3o do patrim\u00f4nio.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Implanta\u00e7\u00e3o de condom\u00ednios</h3>
                        <p>Estrutura\u00e7\u00e3o inicial de cadastros, acessos, rotinas e comunica\u00e7\u00e3o com moradores.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">06</div>
    </div>
    """



def build_page7():
    """FINANCEIRO"""
    return f"""
    <div class="page page-gray">
        <div class="top-bar"></div>
        <div class="geo-bg"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Financeiro</span>
                <h2 style="color:{PRIMARY_DARK};">Mais previsibilidade para a gest\u00e3o condominial</h2>
                <div class="accent-bar"></div>
                <p style="font-size:15px;max-width:520px;color:#444;line-height:1.8;">
                    A organiza\u00e7\u00e3o financeira \u00e9 um dos pontos mais sens\u00edveis de qualquer condom\u00ednio. A Monarca facilita o acompanhamento de receitas, despesas, cobran\u00e7as e pagamentos com informa\u00e7\u00f5es estruturadas e acess\u00edveis.
                </p>
                <div class="grid-3x2" style="margin-top:40px;">
                    <div class="card-teal">
                        <h3>Boletos</h3>
                        <p style="color:rgba(255,255,255,0.85);">Emiss\u00e3o e controle de boletos condominiais de forma organizada.</p>
                    </div>
                    <div class="card-teal">
                        <h3>Presta\u00e7\u00e3o de contas</h3>
                        <p style="color:rgba(255,255,255,0.85);">Relat\u00f3rios claros e acess\u00edveis para acompanhamento financeiro.</p>
                    </div>
                    <div class="card-teal">
                        <h3>Pagamentos</h3>
                        <p style="color:rgba(255,255,255,0.85);">Gest\u00e3o de pagamentos com transpar\u00eancia e controle.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">07</div>
    </div>
    """


def build_page8():
    """SINDICO E CONSELHO"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">S\u00edndico e Conselho</span>
                <h2 style="color:{PRIMARY_DARK};">Suporte para decis\u00f5es mais seguras</h2>
                <div class="accent-bar"></div>
                <p style="font-size:15px;max-width:520px;color:#444;line-height:1.8;">
                    Uma boa administra\u00e7\u00e3o precisa dar base para decis\u00f5es. A Monarca organiza informa\u00e7\u00f5es, acompanha demandas e oferece suporte para que a gest\u00e3o seja conduzida com mais confian\u00e7a.
                </p>
                <div style="background:linear-gradient(135deg, {PRIMARY_DARK}, #0a3040);color:{WHITE};border-radius:16px;padding:30px;margin-top:30px;">
                    <h3 style="color:{ACCENT_LIGHT};font-size:18px;margin-bottom:10px;">Mais m\u00e9todo</h3>
                    <p style="color:rgba(255,255,255,0.85);font-size:14px;">Processos claros reduzem ru\u00eddos, melhoram a comunica\u00e7\u00e3o e fortalecem a governan\u00e7a do condom\u00ednio.</p>
                </div>
                <div class="grid-3x2" style="margin-top:30px;">
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};font-size:14px;">Assessoria especializada</h3>
                        <p>Suporte t\u00e9cnico para a tomada de decis\u00f5es.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};font-size:14px;">Manuten\u00e7\u00e3o predial</h3>
                        <p>Acompanhamento de conserva\u00e7\u00e3o e reparos.</p>
                    </div>
                    <div class="card-outlined">
                        <h3 style="color:{SECONDARY};font-size:14px;">Documenta\u00e7\u00e3o organizada</h3>
                        <p>Acesso f\u00e1cil a atas, editais e registros.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">08</div>
    </div>
    """


def build_page9():
    """APLICATIVO"""
    return f"""
    <div class="page page-dark">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(180deg, {PRIMARY_DARK} 0%, #0a3545 100%);"></div>
        <div style="position:absolute;top:100px;right:-100px;width:400px;height:400px;border:50px solid rgba(0,144,168,0.06);border-radius:50%;"></div>
        <div class="content" style="position:relative;z-index:1;padding-top:80px;">
            <span class="section-tag section-tag-light">Aplicativo</span>
            <h1 style="color:{WHITE};font-size:30px;">Tecnologia a favor da transpar\u00eancia</h1>
            <div class="accent-bar-gold"></div>
            <p style="font-size:15px;color:rgba(255,255,255,0.8);max-width:480px;line-height:1.8;">
                A plataforma digital aproxima a administra\u00e7\u00e3o dos moradores e centraliza informa\u00e7\u00f5es importantes do condom\u00ednio na palma da m\u00e3o.
            </p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:50px;">
                <div class="card-dark" style="text-align:center;padding:30px;">
                    <h3 style="color:{ACCENT_LIGHT};font-size:18px;">Mensagens</h3>
                    <p style="color:rgba(255,255,255,0.7);">Comunica\u00e7\u00e3o direta e organizada.</p>
                </div>
                <div class="card-dark" style="text-align:center;padding:30px;">
                    <h3 style="color:{ACCENT_LIGHT};font-size:18px;">Unidades</h3>
                    <p style="color:rgba(255,255,255,0.7);">Cadastros e informa\u00e7\u00f5es por unidade.</p>
                </div>
                <div class="card-dark" style="text-align:center;padding:30px;">
                    <h3 style="color:{ACCENT_LIGHT};font-size:18px;">Documentos</h3>
                    <p style="color:rgba(255,255,255,0.7);">Atas, regimentos e arquivos centralizados.</p>
                </div>
                <div class="card-dark" style="text-align:center;padding:30px;">
                    <h3 style="color:{ACCENT_LIGHT};font-size:18px;">Boletos</h3>
                    <p style="color:rgba(255,255,255,0.7);">Acesso r\u00e1pido a segunda via e hist\u00f3rico.</p>
                </div>
            </div>
        </div>
        <div class="page-number page-number-light">09</div>
    </div>
    """



def build_page10():
    """MORADORES"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div class="geo-bg-2"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Moradores</span>
                <h2 style="color:{PRIMARY_DARK};">Mais praticidade no dia a dia</h2>
                <div class="accent-bar"></div>
                <p style="font-size:15px;max-width:520px;color:#444;line-height:1.8;">
                    Funcionalidades digitais tornam a rotina mais simples, reduzem d\u00favidas e facilitam o acesso a informa\u00e7\u00f5es e solicita\u00e7\u00f5es do condom\u00ednio.
                </p>
                <div class="feature-grid" style="margin-top:35px;">
                    <div class="feature-item">
                        <h3>Reservas</h3>
                    </div>
                    <div class="feature-item">
                        <h3>Ocorr\u00eancias</h3>
                    </div>
                    <div class="feature-item">
                        <h3>Eventos</h3>
                    </div>
                    <div class="feature-item">
                        <h3>Enquetes</h3>
                    </div>
                    <div class="feature-item">
                        <h3>Achados e perdidos</h3>
                    </div>
                    <div class="feature-item">
                        <h3>Encomendas</h3>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">10</div>
    </div>
    """


def build_page11():
    """SEGURANCA E CONTROLE"""
    return f"""
    <div class="page page-gray">
        <div class="top-bar"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Seguran\u00e7a</span>
                <h2 style="color:{PRIMARY_DARK};">Informa\u00e7\u00f5es importantes bem organizadas</h2>
                <div class="accent-bar"></div>
                <p style="font-size:15px;max-width:520px;color:#444;line-height:1.8;">
                    Cadastros e registros tornam a rotina do condom\u00ednio mais segura, facilitando o controle de acessos, ve\u00edculos, pets, leituras e manuten\u00e7\u00f5es.
                </p>
                <div class="grid-2x3" style="margin-top:30px;">
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Visitantes</h3>
                        <p>Controle de acesso e registro de visitantes.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Ve\u00edculos</h3>
                        <p>Cadastro e identifica\u00e7\u00e3o de ve\u00edculos.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Pets</h3>
                        <p>Registro de animais de estima\u00e7\u00e3o.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Leituras</h3>
                        <p>Registro de consumo individual.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Manuten\u00e7\u00e3o</h3>
                        <p>Acompanhamento de atividades preventivas.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Assembleia virtual</h3>
                        <p>Participa\u00e7\u00e3o remota em delibera\u00e7\u00f5es.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">11</div>
    </div>
    """


def build_page12():
    """PROCESSO DE IMPLANTACAO"""
    return f"""
    <div class="page page-dark">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(160deg, {PRIMARY_DARK} 0%, #0a3040 100%);"></div>
        <div style="position:absolute;top:-50px;right:-50px;width:300px;height:300px;border:40px solid rgba(224,191,140,0.05);border-radius:50%;"></div>
        <div class="content" style="position:relative;z-index:1;padding-top:80px;">
            <span class="section-tag section-tag-light">Implanta\u00e7\u00e3o</span>
            <h2 style="color:{WHITE};font-size:28px;">Implanta\u00e7\u00e3o com come\u00e7o, meio e rotina</h2>
            <div class="accent-bar-gold"></div>
            <p style="font-size:15px;color:rgba(255,255,255,0.8);max-width:500px;line-height:1.8;">
                A implanta\u00e7\u00e3o \u00e9 feita de forma organizada para que o condom\u00ednio comece a operar com cadastros, informa\u00e7\u00f5es e canais preparados.
            </p>
            <div class="timeline" style="margin-top:45px;">
                <div class="timeline-item">
                    <div class="timeline-number">1</div>
                    <p style="color:{WHITE};">Entendimento</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">2</div>
                    <p style="color:{WHITE};">Planejamento</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">3</div>
                    <p style="color:{WHITE};">Formaliza\u00e7\u00e3o</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">4</div>
                    <p style="color:{WHITE};">Cadastros</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">5</div>
                    <p style="color:{WHITE};">Comunica\u00e7\u00e3o</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">6</div>
                    <p style="color:{WHITE};">Opera\u00e7\u00e3o</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">7</div>
                    <p style="color:{WHITE};">Controle</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-number">8</div>
                    <p style="color:{WHITE};">Evolu\u00e7\u00e3o</p>
                </div>
            </div>
        </div>
        <div class="page-number page-number-light">12</div>
    </div>
    """



def build_page13():
    """PARA QUEM"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div class="geo-bg"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Para quem</span>
                <h2 style="color:{PRIMARY_DARK};">Solu\u00e7\u00f5es para diferentes perfis de gest\u00e3o</h2>
                <div class="accent-bar"></div>
                <p style="font-size:15px;max-width:520px;color:#444;line-height:1.8;">
                    A Monarca atende condom\u00ednios que desejam profissionalizar a administra\u00e7\u00e3o e melhorar a rela\u00e7\u00e3o entre gest\u00e3o, conselho e moradores.
                </p>
                <div class="grid-2x3" style="margin-top:30px;">
                    <div class="card-outlined" style="text-align:center;padding:28px;">
                        <h3 style="color:{SECONDARY};">S\u00edndicos</h3>
                    </div>
                    <div class="card-outlined" style="text-align:center;padding:28px;">
                        <h3 style="color:{SECONDARY};">Conselhos</h3>
                    </div>
                    <div class="card-outlined" style="text-align:center;padding:28px;">
                        <h3 style="color:{SECONDARY};">Moradores</h3>
                    </div>
                    <div class="card-outlined" style="text-align:center;padding:28px;">
                        <h3 style="color:{SECONDARY};">Condom\u00ednios residenciais</h3>
                    </div>
                    <div class="card-outlined" style="text-align:center;padding:28px;">
                        <h3 style="color:{SECONDARY};">Condom\u00ednios comerciais</h3>
                    </div>
                    <div class="card-outlined" style="text-align:center;padding:28px;">
                        <h3 style="color:{SECONDARY};">Novos empreendimentos</h3>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">13</div>
    </div>
    """


def build_page14():
    """BENEFICIOS"""
    return f"""
    <div class="page page-gray">
        <div class="top-bar"></div>
        <div class="geo-bg-2"></div>
        <div class="content" style="padding-top:80px;">
            <img src="{LOGO_DATA_URI}" class="logo-small" alt="Monarca">
            <div style="margin-top:40px;">
                <span class="section-tag">Benef\u00edcios</span>
                <h2 style="color:{PRIMARY_DARK};">Uma administra\u00e7\u00e3o que valoriza a experi\u00eancia condominial</h2>
                <div class="accent-bar"></div>
                <div class="grid-2x3" style="margin-top:25px;">
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Menos improviso</h3>
                        <p>Processos definidos reduzem retrabalhos e d\u00favidas recorrentes.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Mais transpar\u00eancia</h3>
                        <p>Informa\u00e7\u00f5es importantes ficam acess\u00edveis de forma organizada.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Decis\u00f5es mais seguras</h3>
                        <p>Dados e registros ajudam s\u00edndico e conselho a agir com confian\u00e7a.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Comunica\u00e7\u00e3o eficiente</h3>
                        <p>Avisos claros reduzem ru\u00eddos e melhoram o alinhamento.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Rotina mais leve</h3>
                        <p>Demandas podem ser registradas e acompanhadas com mais agilidade.</p>
                    </div>
                    <div class="card">
                        <h3 style="color:{SECONDARY};">Gest\u00e3o valorizada</h3>
                        <p>A experi\u00eancia de moradores e gestores se torna mais profissional.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="page-number">14</div>
    </div>
    """


def build_page15():
    """ATUACAO REGIONAL"""
    return f"""
    <div class="page page-dark">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(135deg, {PRIMARY_DARK} 0%, #0a3545 100%);"></div>
        <div style="position:absolute;bottom:-100px;left:-100px;width:350px;height:350px;border:45px solid rgba(0,144,168,0.06);border-radius:50%;"></div>
        <div style="position:absolute;top:80px;right:-60px;width:200px;height:200px;border:25px solid rgba(224,191,140,0.05);border-radius:50%;"></div>
        <div class="content content-centered" style="position:relative;z-index:1;">
            <span class="section-tag section-tag-light">Atua\u00e7\u00e3o</span>
            <h1 style="color:{WHITE};font-size:32px;margin-bottom:20px;">Atua\u00e7\u00e3o regional</h1>
            <div style="width:80px;height:3px;background:{ACCENT};margin:0 auto 30px;"></div>
            <p style="font-size:16px;color:rgba(255,255,255,0.85);max-width:480px;line-height:1.8;">
                Com presen\u00e7a em Porto Belo, Itapema e Tijucas, a Monarca oferece atendimento pr\u00f3ximo para condom\u00ednios que buscam organiza\u00e7\u00e3o, suporte e efici\u00eancia.
            </p>
            <div style="margin-top:40px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:16px;padding:35px 50px;text-align:center;">
                <h3 style="color:{ACCENT_LIGHT};font-size:20px;margin-bottom:15px;letter-spacing:1px;">Porto Belo &mdash; Itapema &mdash; Tijucas</h3>
                <p style="color:rgba(255,255,255,0.7);font-size:14px;">Av. Hironildo Concei\u00e7\u00e3o dos Santos, 973 - Porto Belo/SC</p>
            </div>
        </div>
        <div class="page-number page-number-light">15</div>
    </div>
    """


def build_page16():
    """CTA / CONTATO"""
    return f"""
    <div class="page page-light">
        <div class="top-bar"></div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:120px;background:linear-gradient(0deg, rgba(14,42,53,0.04), transparent);"></div>
        <div class="content content-centered" style="padding-top:60px;">
            <img src="{LOGO_DATA_URI}" alt="Monarca" style="width:160px;margin-bottom:40px;">
            <h1 style="font-size:26px;color:{PRIMARY_DARK};max-width:480px;line-height:1.3;">Pronto para elevar o padr\u00e3o da gest\u00e3o do seu condom\u00ednio?</h1>
            <div style="width:60px;height:3px;background:{SECONDARY};margin:20px auto;"></div>
            <p style="font-size:18px;color:{SECONDARY};font-weight:600;margin-bottom:10px;">Fale com a Monarca.</p>
            <p style="font-size:14px;color:#555;max-width:420px;line-height:1.7;margin-bottom:30px;">
                Conte com uma administradora pr\u00f3xima, organizada e transparente para cuidar da rotina condominial com mais efici\u00eancia e seguran\u00e7a.
            </p>
            <div style="background:{PRIMARY_DARK};color:{WHITE};border-radius:16px;padding:35px 50px;text-align:center;width:100%;max-width:450px;">
                <div style="margin-bottom:18px;">
                    <p style="font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:{ACCENT_LIGHT};margin-bottom:5px;">Telefone</p>
                    <p style="font-size:18px;font-weight:600;color:{WHITE};">47 3405 4646</p>
                </div>
                <div style="margin-bottom:18px;">
                    <p style="font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:{ACCENT_LIGHT};margin-bottom:5px;">Localiza\u00e7\u00e3o</p>
                    <p style="font-size:16px;color:{WHITE};">Porto Belo - SC</p>
                </div>
                <div>
                    <p style="font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:{ACCENT_LIGHT};margin-bottom:5px;">Endere\u00e7o</p>
                    <p style="font-size:14px;color:rgba(255,255,255,0.85);">Av. Hironildo Concei\u00e7\u00e3o dos Santos, 973<br>Porto Belo - SC</p>
                </div>
            </div>
        </div>
        <div class="page-number">16</div>
    </div>
    """



def build_html():
    """Build the complete HTML document."""
    css = build_css()
    pages = [
        build_page1(),
        build_page2(),
        build_page3(),
        build_page4(),
        build_page5(),
        build_page6(),
        build_page7(),
        build_page8(),
        build_page9(),
        build_page10(),
        build_page11(),
        build_page12(),
        build_page13(),
        build_page14(),
        build_page15(),
        build_page16(),
    ]

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Proposta Comercial - Monarca Administradora</title>
    <style>
    {css}
    </style>
</head>
<body>
{''.join(pages)}
</body>
</html>"""
    return html


def main():
    print("Gerando Proposta Comercial Monarca...")
    print(f"Logo: {LOGO_PATH}")
    print(f"Output: {OUTPUT_PATH}")

    html_content = build_html()

    # Save HTML for debugging (optional)
    html_path = os.path.join(SCRIPT_DIR, "proposta_debug.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML salvo em: {html_path}")

    # Generate PDF with WeasyPrint
    print("Gerando PDF com WeasyPrint...")
    html_doc = HTML(string=html_content, base_url=SCRIPT_DIR)
    html_doc.write_pdf(OUTPUT_PATH)
    print(f"PDF gerado com sucesso: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

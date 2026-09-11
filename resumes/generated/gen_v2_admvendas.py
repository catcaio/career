#!/usr/bin/env python3
"""Curriculo 915050 V2 — CAUSA CERTA / Analista Adm Vendas.
Motor: skill resume-document-design (tokens INK/MUTED/ACCENT/RULE, escala V2).
Mesmos fatos do V1 (spec-admvendas-causacerta-v1.json); sem metrica de faturamento.
Gera PDF (reportlab) + DOCX (python-docx) + spec JSON V2.
Uso: python3 gen_v2_admvendas.py
"""
import json, os
from copy import deepcopy

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_OUT = os.path.join(OUT_DIR, "Rafa_Nascimento_Curriculo_CausaCerta_AnalistaAdmVendas_V2.pdf")
DOCX_OUT = os.path.join(OUT_DIR, "Rafa_Nascimento_Curriculo_CausaCerta_AnalistaAdmVendas_V2.docx")
SPEC_OUT = os.path.join(OUT_DIR, "spec-admvendas-causacerta-v2.json")

INK, MUTED, ACCENT, RULE = "23272F", "5A6270", "1F5C4E", "C9CFD6"

CONTENT = {
    "name": "CAIO RAFAEL BARROS DO NASCIMENTO",
    "role": "Analista Administrativo de Vendas  |  Rotinas Administrativas  |  Comercial B2B e Atendimento",
    "contact": "Nova Palhoça — Palhoça/SC  |  (48) 99153-2952  |  cr_bn20@hotmail.com  |  linkedin.com/in/rafael-brasiliae",
    "availability": "Disponibilidade: 100% home office ou presencial (Grande Florianópolis)  |  Viagens: disponível quando necessário",
    "sections": [
        {"title": "RESUMO PROFISSIONAL", "body": [
            "Profissional administrativo e comercial com mais de 5 anos de atuação entre rotinas administrativas, vendas B2B e atendimento ao cliente. Experiência com conferência e manutenção de contratos, organização de documentação, acompanhamento de status e prazos, uso de planilhas e sistemas internos (ERP) e atuação como elo entre áreas comercial, operacional e parceiros. Perfil organizado, comunicativo e orientado a processos confiáveis."
        ]},
        {"title": "COMPETÊNCIAS-CHAVE", "bullets": [
            "Contratos e documentação: conferência de contratos, coleta e organização de documentos, acompanhamento de status e envio dentro de prazos",
            "Rotinas administrativas: planilhas, sistemas internos e ERP (Olist/Tiny), organização de bases operacionais e suporte a financeiro, compras, estoque e despacho",
            "Comercial e atendimento B2B: prospecção, negociação, atendimento a clientes empresariais, retenção e contorno de objeções, comunicação via WhatsApp, e-mail, telefone e canais digitais",
            "Processos: estruturação e digitalização de rotinas de atendimento, orçamento e vendas; treinamento de colaboradores em processos operacionais",
        ]},
        {"title": "EXPERIÊNCIA PROFISSIONAL", "jobs": [
            {"company": "LOJACOND (Store / Equipamentos) — Palhoça/SC  |  Mar/2021 – Abr/2026",
             "roles": [
                {"role": "Gestor de E-commerce e Operações Digitais  |  Dez/2022 – Abr/2026", "bullets": [
                    "Gestão comercial e administrativa de e-commerce e marketplaces: vendas, pedidos, estoque, preços, contratos com transportadoras e indicadores de desempenho",
                    "Administração de aproximadamente 2 mil SKUs e base de 7 mil clientes, com organização e consistência das informações comerciais e operacionais",
                    "Integração entre e-commerce, ERP (Olist/Tiny), pagamentos, frete, estoque e canais de atendimento; acompanhamento do fluxo completo do pedido (venda, faturamento, expedição, entrega e pós-venda)",
                ]},
                {"role": "Assistente Administrativo e Comercial  |  Mar/2021 – Dez/2022", "bullets": [
                    "Ingresso como estagiário (graduação em Administração), efetivado em CLT após 3 meses; atuação direta com gerência e direção",
                    "Estruturação e digitalização dos processos de atendimento, orçamento e vendas B2B, integrando WhatsApp, e-mail, telefone, site e canais digitais",
                    "Negociação e manutenção de contratos, tabelas e condições comerciais com transportadoras; prospecção e negociação B2B (condomínios, empresas privadas e órgãos públicos), com negociações de até R$ 70 mil",
                    "Organização e atualização de sistemas e bases operacionais, incluindo migração de processos para Olist/Tiny",
                ]},
             ]},
            {"company": "FLEX CONTACT CENTER — Florianópolis/SC  |  Fev/2018 – Dez/2020",
             "roles": [
                {"role": None, "bullets": [
                    "Agente de Retenção B2B: atendimento a clientes empresariais, orientação e negociação orientada por metas, escuta ativa e contorno de objeções (pacote Claro NET)",
                ]},
             ]},
            {"company": "MG VIDROS — AUTO GLASS  |  2013 – 2014",
             "roles": [
                {"role": None, "bullets": [
                    "Auxiliar de Vendedor Técnico / Jovem Aprendiz: atendimento, elaboração de orçamentos e apoio à venda técnica no setor automotivo",
                ]},
             ]},
        ]},
        {"title": "FORMAÇÃO", "bullets": [
            "Administração — 3 anos cursados",
            "Análise e Desenvolvimento de Sistemas — UNISUL (cursando, conclusão prevista 2027)",
            "Assistente Administrativo — S.O.S Educação Profissional (2012, 18 meses)",
            "Ensino Médio — completo",
        ]},
        {"title": "IDIOMAS", "bullets": [
            "Português nativo  |  Inglês avançado",
        ]},
    ],
}


def build_pdf():
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, KeepTogether,
                                    PageTemplate, Paragraph, Spacer)

    ink, muted, accent, rule = (HexColor("#" + c) for c in (INK, MUTED, ACCENT, RULE))
    s_name = ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=ink, spaceAfter=2)
    s_role = ParagraphStyle("Role", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=ink, spaceAfter=4)
    s_contact = ParagraphStyle("Contact", fontName="Helvetica", fontSize=8.5, leading=11, textColor=muted, spaceAfter=2)
    s_avail = ParagraphStyle("Avail", fontName="Helvetica", fontSize=8.5, leading=11, textColor=muted, spaceAfter=2)
    s_sec = ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=accent, spaceBefore=16, spaceAfter=4)
    s_co = ParagraphStyle("Company", fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=ink, spaceBefore=12, spaceAfter=1)
    s_job = ParagraphStyle("Job", fontName="Helvetica-BoldOblique", fontSize=10, leading=13, textColor=ink, spaceAfter=2)
    s_body = ParagraphStyle("Body", fontName="Helvetica", fontSize=10, leading=15.5, textColor=ink, spaceAfter=2)
    s_bul = ParagraphStyle("Bullet", parent=s_body, leftIndent=12, firstLineIndent=0, spaceAfter=5,
                           bulletIndent=4)

    _TOTAL = {"n": 0}

    def footer(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 8)
        canv.setFillColor(muted)
        total = _TOTAL["n"] or doc.page
        canv.drawCentredString(A4[0] / 2, 12 * mm, f"Página {doc.page} de {total}")
        canv.restoreState()

    def _build(out, story):
        doc = BaseDocTemplate(out, pagesize=A4,
                              leftMargin=20 * mm, rightMargin=20 * mm,
                              topMargin=18 * mm, bottomMargin=18 * mm,
                              title="Currículo - Caio Rafael Barros do Nascimento - Analista Administrativo de Vendas",
                              author="Hermes Career Agent")
        frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
        doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=footer)])
        doc.build(story)

    def _make_story():
        st = [Paragraph(CONTENT["name"], s_name),
              Paragraph(CONTENT["role"], s_role),
              HRFlowable(width="100%", thickness=1.2, color=accent, spaceAfter=4),
              Paragraph(CONTENT["contact"], s_contact),
              Paragraph(CONTENT["availability"], s_avail)]
        for sec in CONTENT["sections"]:
            st.append(Paragraph(sec["title"], s_sec))
            st.append(HRFlowable(width="100%", thickness=0.6, color=rule, spaceAfter=4))
            block = []
            for b in sec.get("body", []):
                block.append(Paragraph(b, s_body))
            for b in sec.get("bullets", []):
                block.append(Paragraph(f"- {b}", s_bul, bulletText=""))
            for job in sec.get("jobs", []):
                jb = [Paragraph(job["company"], s_co)]
                for r in job["roles"]:
                    if r["role"]:
                        jb.append(Paragraph(r["role"], s_job))
                    for b in r["bullets"]:
                        jb.append(Paragraph(f"- {b}", s_bul, bulletText=""))
                block.append(KeepTogether(jb))
            if sec["title"] in ("FORMAÇÃO", "IDIOMAS"):
                st.append(KeepTogether(block))
            else:
                st.extend(block)
        return st

    _build(PDF_OUT + ".pass1.pdf", _make_story())
    from pypdf import PdfReader
    _TOTAL["n"] = len(PdfReader(PDF_OUT + ".pass1.pdf").pages)
    _build(PDF_OUT, _make_story())
    try: os.remove(PDF_OUT + ".pass1.pdf")
    except OSError: pass
    return PDF_OUT


def _docx_border_bottom(paragraph, color="C9CFD6", sz="6"):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    pPr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), sz)
    bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), color)
    pbdr.append(bottom); pPr.append(pbdr)


def _docx_footer_numbers(doc):
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    sec = doc.sections[0]
    fp = sec.footer.paragraphs[0]
    fp.alignment = 2  # center=2? 1=center; usar 2=right? -> 1 center
    fp.alignment = 1
    fp.text = ""
    r = fp.add_run(); r.font.size = __import__("docx").shared.Pt(8); r.font.color.rgb = __import__("docx").shared.RGBColor(0x5A, 0x62, 0x70)
    def field(run, instr):
        f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
        it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = instr
        f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
        run._r.append(f1); run._r.append(it); run._r.append(f2)
    r2 = fp.add_run("Página "); r2.font.size = __import__("docx").shared.Pt(8)
    r2.font.color.rgb = __import__("docx").shared.RGBColor(0x5A, 0x62, 0x70)
    field(fp.add_run(), "PAGE")
    r3 = fp.add_run(" de "); r3.font.size = __import__("docx").shared.Pt(8)
    r3.font.color.rgb = __import__("docx").shared.RGBColor(0x5A, 0x62, 0x70)
    field(fp.add_run(), "NUMPAGES")


def build_docx():
    from docx import Document
    from docx.shared import Pt, Mm, RGBColor
    from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
    doc = Document()
    for sec in doc.sections:
        sec.page_width, sec.page_height = Mm(210), Mm(297)
        sec.left_margin, sec.right_margin = Mm(20), Mm(20)
        sec.top_margin, sec.bottom_margin = Mm(18), Mm(18)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"; style.font.size = Pt(10)
    style.font.color.rgb = RGBColor(0x23, 0x27, 0x2F)
    style.paragraph_format.space_after = Pt(2)
    style.paragraph_format.widow_control = True

    def para(text, bold=False, italic=False, size=10, color=(0x23, 0x27, 0x2F), before=0, after=2, align=None):
        p = doc.add_paragraph()
        run = p.add_run(text); run.bold = bold; run.italic = italic
        run.font.size = Pt(size); run.font.color.rgb = RGBColor(*color)
        p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
        if align is not None: p.alignment = align
        return p

    para(CONTENT["name"], bold=True, size=18, after=2)
    p = para(CONTENT["role"], bold=True, size=10.5, after=4)
    _docx_border_bottom(p, color=ACCENT, sz="9")
    para(CONTENT["contact"], size=8.5, color=(0x5A, 0x62, 0x70), after=2)
    para(CONTENT["availability"], size=8.5, color=(0x5A, 0x62, 0x70), after=2)
    for sec in CONTENT["sections"]:
        p = para(sec["title"], bold=True, size=11, color=(0x1F, 0x5C, 0x4E), before=10, after=4)
        _docx_border_bottom(p, color=RULE)
        for b in sec.get("body", []):
            para(b)
        for b in sec.get("bullets", []):
            bp = para(f"- {b}")
            bp.paragraph_format.left_indent = Mm(4)
        for job in sec.get("jobs", []):
            para(job["company"], bold=True, size=10, before=6, after=1)
            for r in job["roles"]:
                if r["role"]:
                    para(r["role"], bold=True, italic=True, size=10, after=2)
                for b in r["bullets"]:
                    bp = para(f"- {b}")
                    bp.paragraph_format.left_indent = Mm(4)
    _docx_footer_numbers(doc)
    doc.save(DOCX_OUT)
    return DOCX_OUT


def write_spec():
    spec = {"title": "Currículo - Caio Rafael Barros do Nascimento - Analista Administrativo de Vendas (V2)",
            "author": "Hermes Career Agent", "version": "V2", "page_size": "A4",
            "design_tokens": {"INK": INK, "MUTED": MUTED, "ACCENT": ACCENT, "RULE": RULE},
            "type_scale": "skill resume-document-design, secao 2 (base V2)",
            "content": deepcopy(CONTENT)}
    json.dump(spec, open(SPEC_OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return SPEC_OUT


if __name__ == "__main__":
    print("PDF:", build_pdf())
    print("DOCX:", build_docx())
    print("SPEC:", write_spec())

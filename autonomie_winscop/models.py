# coding: utf-8
from sqlalchemy import Column, Date, Enum, Float, Index, Integer, Numeric, String, Table, Text, Time, text
from autonomie_winscop import BASE, metadata


class Absence(BASE):
    __tablename__ = 'absences'

    id_absence = Column(Integer, primary_key=True)
    id_salarie = Column(Integer, nullable=False)
    type_salarie = Column(String(255), nullable=False)
    type_absence = Column(String(255), nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    demi_debut = Column(Integer, nullable=False)
    demi_fin = Column(Integer, nullable=False)
    nb_jours_absence = Column(Float, nullable=False)
    nb_heures_absence = Column(Float, nullable=False)
    commentaire = Column(String(255), nullable=False)


class Achat(BASE):
    __tablename__ = 'achats'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'mois', 'annee'),
    )

    id_achat = Column(Integer, primary_key=True)
    id_facture = Column(Integer, nullable=False)
    id_porteur = Column(Integer, nullable=False)
    mois = Column(Integer, nullable=False)
    annee = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    id_fournisseur = Column(Integer, nullable=False)
    id_chantier = Column(Integer, nullable=False)
    num_facture = Column(String(255), nullable=False)
    libelle = Column(String(255), nullable=False)
    compte = Column(String(13), nullable=False)
    taux_tva = Column(Float, nullable=False)
    montant_ht = Column(Numeric(16, 4), nullable=False)
    montant_cae = Column(Numeric(16, 4), nullable=False)
    reglement_cae = Column(String(255), nullable=False)
    paye = Column(Integer, nullable=False)
    valide = Column(Integer, nullable=False)
    date_export = Column(Date, nullable=False, index=True, server_default=text("'0000-00-00'"))
    num_piece = Column(String(255), nullable=False, index=True)
    num_ordre = Column(Integer, nullable=False)


class Acteur(BASE):
    __tablename__ = 'acteurs'

    id_acteur = Column(Integer, primary_key=True)
    civilite = Column(String(255), nullable=False)
    nom = Column(String(255), nullable=False)
    prenom = Column(String(255), nullable=False)
    organisme = Column(String(255), nullable=False)
    fonction = Column(String(255), nullable=False)
    fonction_detail = Column(String(255), nullable=False)
    adresse = Column(String(255), nullable=False)
    adresse_suite = Column(String(255), nullable=False)
    cp = Column(String(5), nullable=False)
    ville = Column(String(255), nullable=False)
    tel_1 = Column(String(18), nullable=False)
    tel_2 = Column(String(18), nullable=False)
    tel_port = Column(String(18), nullable=False)
    fax = Column(String(18), nullable=False)
    mail = Column(String(255), nullable=False)
    obs = Column(Text, nullable=False)
    is_financeur = Column(Integer, nullable=False)
    is_institutionnel = Column(Integer, nullable=False)
    is_part_actif = Column(Integer, nullable=False)
    is_prescripteur = Column(Integer, nullable=False)
    is_coop = Column(Integer, nullable=False)
    is_frn = Column(Integer, nullable=False)
    is_comite_tech = Column(Integer, nullable=False)
    is_comite_pilotage = Column(Integer, nullable=False)
    is_informateur = Column(Integer, nullable=False)
    is_groupe_crea = Column(Integer, nullable=False)
    is_media = Column(Integer, nullable=False)
    is_part_social = Column(Integer, nullable=False)
    is_client = Column(Integer, nullable=False)
    is_assureur = Column(Integer, nullable=False)
    is_employeur = Column(Integer, nullable=False)


class Alerte(BASE):
    __tablename__ = 'alertes'

    id_alerte = Column(Integer, primary_key=True)
    id_permanent = Column(Integer, nullable=False)
    id_porteur = Column(Integer, nullable=False)
    id_parcours = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    date_echeance = Column(Date, nullable=False)
    libelle = Column(String(255), nullable=False)
    lue = Column(Integer, nullable=False, server_default=text("'0'"))


class AlertesFacturesAuto(BASE):
    __tablename__ = 'alertes_factures_auto'

    id_paiement = Column(String(30), primary_key=True, server_default=text("''"))
    verifiee = Column(Integer, nullable=False)


class AlertesPorteur(BASE):
    __tablename__ = 'alertes_porteurs'

    id_alerte = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    type = Column(String(255), nullable=False)
    libelle = Column(String(255), nullable=False)
    details = Column(Text, nullable=False)
    lue = Column(Integer, nullable=False)


class AlertesStat(BASE):
    __tablename__ = 'alertes_stats'

    semestre = Column(Integer, primary_key=True, nullable=False)
    annee = Column(Integer, primary_key=True, nullable=False)
    next_alerte = Column(Date, nullable=False)
    stats_ok = Column(Integer, nullable=False)


class AvanceTravaux(BASE):
    __tablename__ = 'avance_travaux'

    id_c_facture_uo = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_facture = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_paiement = Column(String(30), primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    pourcentage = Column(Float, nullable=False, server_default=text("'0'"))


class Base(BASE):
    __tablename__ = 'bases'

    id_base = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False, server_default=text("''"))
    formule = Column(String(255), nullable=False, server_default=text("''"))


class CDevisCharge(BASE):
    __tablename__ = 'c_devis_charges'

    id_chantier = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_devis = Column(String(30), primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    tech_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_4_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_4_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_4_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_4_f = Column(Float, nullable=False, server_default=text("'0'"))
    comm_m = Column(Float, nullable=False, server_default=text("'0'"))
    comm_f = Column(Float, nullable=False, server_default=text("'0'"))
    autre_m = Column(Float, nullable=False, server_default=text("'0'"))
    autre_f = Column(Float, nullable=False, server_default=text("'0'"))


class CDevisMateriaux(BASE):
    __tablename__ = 'c_devis_materiaux'
    __table_args__ = (
        Index('id_devis', 'id_devis', 'id_uo'),
    )

    id_c_devis_mat = Column(Integer, primary_key=True)
    id_materiel = Column(Integer, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_devis = Column(String(30), nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(50), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_famille = Column(Integer, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    id_c_devis_uo = Column(Integer, nullable=False, server_default=text("'0'"))


class CDevisMaterielAff(BASE):
    __tablename__ = 'c_devis_materiel_aff'
    __table_args__ = (
        Index('id_devis', 'id_devis', 'id_uo'),
    )

    id_c_devis_materiel_aff = Column(Integer, primary_key=True)
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    id_devis = Column(String(30), nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_mat_aff = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(255), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    id_c_devis_uo = Column(Integer, nullable=False, server_default=text("'0'"))


class CDevisUo(BASE):
    __tablename__ = 'c_devis_uo'

    id_c_devis_uo = Column(Integer, primary_key=True)
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_devis = Column(String(30), nullable=False, index=True, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    designation = Column(String(255), nullable=False, server_default=text("''"))
    prix_mo = Column(Numeric(16, 4), nullable=False)
    qt_mo = Column(Float, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    prix = Column(Numeric(16, 4), nullable=False)
    qt_uo = Column(Float, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    description = Column(Text, nullable=False)
    indice = Column(Integer, nullable=False, server_default=text("'0'"))
    simple = Column(Integer, nullable=False)
    simple_ht = Column(Numeric(10, 4), nullable=False)


class CEdpMateriaux(BASE):
    __tablename__ = 'c_edp_materiaux'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'id_edp', 'id_chantier', 'id_uo'),
    )

    id_c_edp_mat = Column(Integer, primary_key=True)
    id_materiel = Column(Integer, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_edp = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(50), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_famille = Column(Integer, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    id_c_edp_uo = Column(Integer, nullable=False, server_default=text("'0'"))


class CEdpMaterielAff(BASE):
    __tablename__ = 'c_edp_materiel_aff'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'id_chantier', 'id_edp', 'id_uo'),
    )

    id_c_edp_materiel_aff = Column(Integer, primary_key=True)
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    id_edp = Column(Integer, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_mat_aff = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(255), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    id_c_edp_uo = Column(Integer, nullable=False, server_default=text("'0'"))


class CEdpUo(BASE):
    __tablename__ = 'c_edp_uo'
    __table_args__ = (
        Index('id_chantier', 'id_chantier', 'id_porteur', 'id_edp'),
    )

    id_c_edp_uo = Column(Integer, primary_key=True)
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_edp = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    designation = Column(String(255), nullable=False, server_default=text("''"))
    prix_mo = Column(Numeric(16, 4), nullable=False)
    qt_mo = Column(Float, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    prix = Column(Numeric(16, 4), nullable=False)
    qt_uo = Column(Float, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    description = Column(Text, nullable=False)
    indice = Column(Integer, nullable=False, server_default=text("'0'"))
    simple = Column(Integer, nullable=False)
    simple_ht = Column(Numeric(16, 4), nullable=False)


class CFactureCharge(BASE):
    __tablename__ = 'c_facture_charges'

    id_chantier = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_facture = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    tech_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_4_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_4_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_4_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_4_f = Column(Float, nullable=False, server_default=text("'0'"))
    comm_m = Column(Float, nullable=False, server_default=text("'0'"))
    comm_f = Column(Float, nullable=False, server_default=text("'0'"))
    autre_m = Column(Float, nullable=False, server_default=text("'0'"))
    autre_f = Column(Float, nullable=False, server_default=text("'0'"))


class CFactureMateriaux(BASE):
    __tablename__ = 'c_facture_materiaux'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'id_chantier', 'id_facture', 'id_uo'),
    )

    id_c_facture_mat = Column(Integer, primary_key=True)
    id_materiel = Column(Integer, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_facture = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(50), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_famille = Column(Integer, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    id_c_facture_uo = Column(Integer, nullable=False, server_default=text("'0'"))


class CFactureMaterielAff(BASE):
    __tablename__ = 'c_facture_materiel_aff'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'id_chantier', 'id_facture', 'id_uo'),
    )

    id_c_facture_materiel_aff = Column(Integer, primary_key=True)
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    id_facture = Column(Integer, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_mat_aff = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(255), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    id_c_facture_uo = Column(Integer, nullable=False, server_default=text("'0'"))


class CFactureUo(BASE):
    __tablename__ = 'c_facture_uo'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'id_chantier', 'id_facture'),
    )

    id_c_facture_uo = Column(Integer, primary_key=True)
    id_uo = Column(String(15), nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_facture = Column(Integer, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    designation = Column(String(255), nullable=False, server_default=text("''"))
    prix_mo = Column(Numeric(16, 4), nullable=False)
    qt_mo = Column(Float, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    prix = Column(Numeric(16, 4), nullable=False)
    qt_uo = Column(Float, nullable=False, server_default=text("'0'"))
    qt = Column(Float, nullable=False, server_default=text("'0'"))
    description = Column(Text, nullable=False)
    indice = Column(Integer, nullable=False, server_default=text("'0'"))
    simple = Column(Integer, nullable=False)
    simple_ht = Column(Numeric(10, 4), nullable=False)


class Categorie(BASE):
    __tablename__ = 'categorie'
    __table_args__ = (
        Index('num_cpta_7', 'num_cpta_7', 'categorie'),
    )

    id_categorie = Column(Integer, primary_key=True)
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)
    lib_grp = Column(String(255), nullable=False)


class Chantiers2(BASE):
    __tablename__ = 'chantiers2'

    id_chantier = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_client = Column(Integer, nullable=False, server_default=text("'0'"))
    adresse = Column(String(255), nullable=False, server_default=text("''"))
    adresse_s = Column(String(255), nullable=False, server_default=text("''"))
    cp = Column(String(5), nullable=False, server_default=text("''"))
    ville = Column(String(255), nullable=False, server_default=text("''"))
    description = Column(Text, nullable=False)
    id_maitre = Column(Integer, nullable=False, server_default=text("'0'"))
    kmDomicile = Column(Float, nullable=False, server_default=text("'0'"))
    kmFournisseur = Column(Float, nullable=False, server_default=text("'0'"))
    adr_client = Column(Integer, nullable=False, server_default=text("'0'"))
    date_deb = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    date_fin = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    transfert = Column(Integer, nullable=False)


class Charge(BASE):
    __tablename__ = 'charges'

    id_chantier = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_edp = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    tech_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    tech_4_m = Column(Float, nullable=False, server_default=text("'0'"))
    tech_4_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    sst_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    sst_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_1_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_1_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_2_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_2_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_3_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_3_f = Column(Float, nullable=False, server_default=text("'0'"))
    loc_4_m = Column(Float, nullable=False, server_default=text("'0'"))
    loc_4_f = Column(Float, nullable=False, server_default=text("'0'"))
    comm_m = Column(Float, nullable=False, server_default=text("'0'"))
    comm_f = Column(Float, nullable=False, server_default=text("'0'"))
    autre_m = Column(Float, nullable=False, server_default=text("'0'"))
    autre_f = Column(Float, nullable=False, server_default=text("'0'"))


class Client(BASE):
    __tablename__ = 'clients'

    id_client = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    raison_sociale = Column(String(255), nullable=False)
    genre = Column(String(255), nullable=False)
    nom = Column(String(255), nullable=False)
    prenom = Column(String(255), nullable=False)
    adresse = Column(String(255), nullable=False, server_default=text("''"))
    adresse_s = Column(String(255), nullable=False, server_default=text("''"))
    cp = Column(String(6), nullable=False, server_default=text("''"))
    ville = Column(String(255), nullable=False, server_default=text("''"))
    mail = Column(String(255), nullable=False, server_default=text("''"))
    tel = Column(String(18), nullable=False)
    fax = Column(String(18), nullable=False)
    travail = Column(String(18), nullable=False)
    portable = Column(String(18), nullable=False)
    num_tvaintra = Column(String(255), nullable=False)
    remarques = Column(Text, nullable=False)
    num_cpta_411 = Column(String(13), nullable=False)
    num_cpta_411_tiers = Column(String(17), nullable=False)
    pays = Column(String(255), nullable=False, server_default=text("'FRANCE'"))
    site_web = Column(String(255), nullable=False)


class CodifActionsRsa(BASE):
    __tablename__ = 'codif_actions_rsa'

    action = Column(String(255), primary_key=True)


class CodifCentreEnregistrement(BASE):
    __tablename__ = 'codif_centre_enregistrement'

    centre = Column(String(255), primary_key=True)


class CodifCivilite(BASE):
    __tablename__ = 'codif_civilites'

    civilite = Column(String(255), primary_key=True)
    civilite_abr = Column(String(8), nullable=False)
    sexe = Column(String(1), nullable=False)


t_codif_criteres = Table(
    'codif_criteres', metadata,
    Column('critere_1', String(255), nullable=False),
    Column('critere_2', String(255), nullable=False),
    Column('critere_3', String(255), nullable=False),
    Column('critere_4', String(255), nullable=False),
    Column('critere_5', String(255), nullable=False),
    Column('critere_6', String(255), nullable=False),
    Column('critere_7', String(255), nullable=False),
    Column('critere_8', String(255), nullable=False),
    Column('critere_9', String(255), nullable=False),
    Column('critere_10', String(255), nullable=False),
    Column('critere_11', String(255), nullable=False),
    Column('critere_12', String(255), nullable=False)
)


class CodifCriteresFact(BASE):
    __tablename__ = 'codif_criteres_fact'

    id_critere = Column(Integer, primary_key=True, nullable=False)
    id_option = Column(Integer, primary_key=True, nullable=False)
    libelle = Column(String(255), nullable=False)
    item = Column(String(255), nullable=False)


class CodifDept(BASE):
    __tablename__ = 'codif_depts'

    num_dept = Column(String(3), primary_key=True)
    nom = Column(String(255), nullable=False)


class CodifDroit(BASE):
    __tablename__ = 'codif_droits'

    droit = Column(String(255), primary_key=True)
    libelle = Column(String(255), nullable=False)


class CodifMesuresInsertion(BASE):
    __tablename__ = 'codif_mesures_insertion'

    mesure = Column(String(255), primary_key=True)


class CodifMotifsSortie(BASE):
    __tablename__ = 'codif_motifs_sortie'

    motif = Column(String(255), primary_key=True)


class CodifNationalite(BASE):
    __tablename__ = 'codif_nationalites'

    nationalite = Column(String(255), primary_key=True)
    code = Column(String(2), nullable=False)


class CodifNiveauForm(BASE):
    __tablename__ = 'codif_niveau_form'

    niveau_form = Column(String(255), primary_key=True)


class CodifPosition(BASE):
    __tablename__ = 'codif_positions'

    position = Column(String(255), primary_key=True)


class CodifRessource(BASE):
    __tablename__ = 'codif_ressources'

    ressource = Column(String(255), primary_key=True)


class CodifSecteurAct(BASE):
    __tablename__ = 'codif_secteur_act'

    activite = Column(String(255), primary_key=True)


class CodifSituation(BASE):
    __tablename__ = 'codif_situation'

    situation = Column(String(255), primary_key=True)
    libelle = Column(String(255), nullable=False)


class CodifSituationDetail(BASE):
    __tablename__ = 'codif_situation_detail'

    situation = Column(String(255), primary_key=True, nullable=False)
    detail = Column(String(255), primary_key=True, nullable=False)


class CodifSituationFam(BASE):
    __tablename__ = 'codif_situation_fam'

    situation = Column(String(255), primary_key=True)


class CodifStatutDirigeant(BASE):
    __tablename__ = 'codif_statut_dirigeant'

    statut = Column(String(255), primary_key=True)


class CodifStatutJuridique(BASE):
    __tablename__ = 'codif_statut_juridique'

    statut = Column(String(255), primary_key=True)


class CodifStatut(BASE):
    __tablename__ = 'codif_statuts'

    statut = Column(String(255), primary_key=True)


class CodifTypesCoti(BASE):
    __tablename__ = 'codif_types_cotis'

    id_type_cotis = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False, server_default=text("''"))


class CongesAcqui(BASE):
    __tablename__ = 'conges_acquis'

    id_salarie = Column(Integer, primary_key=True, nullable=False)
    type_salarie = Column(Enum(u'entrepreneur', u'permanent'), primary_key=True, nullable=False)
    annee = Column(Integer, primary_key=True, nullable=False)
    nb_jours = Column(Integer, nullable=False)


class Constante(BASE):
    __tablename__ = 'constantes'

    id_constantes = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    plafond = Column(Float, nullable=False, server_default=text("'0'"))
    temps_plein = Column(Float, nullable=False, server_default=text("'0'"))
    smic_h = Column(Float, nullable=False, server_default=text("'0'"))
    gmp = Column(Float, nullable=False, server_default=text("'0'"))
    prime_panier = Column(Float, nullable=False, server_default=text("'0'"))
    prime_transport = Column(Float, nullable=False, server_default=text("'0'"))
    trajet_zone_1 = Column(Float, nullable=False, server_default=text("'0'"))
    trajet_zone_2 = Column(Float, nullable=False, server_default=text("'0'"))
    trajet_zone_3 = Column(Float, nullable=False, server_default=text("'0'"))
    trajet_zone_4 = Column(Float, nullable=False, server_default=text("'0'"))
    trajet_zone_5 = Column(Float, nullable=False, server_default=text("'0'"))
    taux_intemperies = Column(Float, nullable=False)


class ContratsRsa(BASE):
    __tablename__ = 'contrats_rsa'

    id_contrat = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    date_deb = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    date_val = Column(Date, nullable=False)
    duree = Column(String(255), nullable=False)
    referent = Column(String(255), nullable=False)
    mesure = Column(String(255), nullable=False)


class Cooperative(BASE):
    __tablename__ = 'cooperative'

    raison_sociale = Column(String(255), primary_key=True)
    complement = Column(String(255), nullable=False)
    forme_juridique = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    type_detail = Column(String(255), nullable=False)
    is_scop = Column(Integer, nullable=False)
    is_asso = Column(Integer, nullable=False)
    is_etabl = Column(Integer, nullable=False)
    is_filiale = Column(Integer, nullable=False)
    date_creation = Column(Date, nullable=False)
    civilite_gerant = Column(String(255), nullable=False)
    nom_gerant = Column(String(255), nullable=False)
    date_gerant = Column(Date, nullable=False)
    duree_gerant = Column(Integer, nullable=False)
    territorialisation = Column(String(255), nullable=False)
    essaimage = Column(String(255), nullable=False)
    adresse = Column(String(255), nullable=False)
    adresse_suite = Column(String(255), nullable=False)
    cp = Column(String(5), nullable=False)
    ville = Column(String(255), nullable=False)
    tel_1 = Column(String(18), nullable=False)
    tel_2 = Column(String(18), nullable=False)
    tel_port = Column(String(18), nullable=False)
    fax = Column(String(18), nullable=False)
    mail_1 = Column(String(255), nullable=False)
    mail_2 = Column(String(255), nullable=False)
    num_siret = Column(String(17), nullable=False)
    code_ape = Column(String(5), nullable=False)
    num_tvaintra = Column(String(255), nullable=False)
    num_cnil = Column(String(255), nullable=False)
    code_cpta = Column(String(30), nullable=False)
    assurance = Column(Integer, nullable=False)
    log_compta = Column(String(255), nullable=False)
    bdd_compta = Column(String(255), nullable=False)
    maj_compta = Column(Date, nullable=False)
    tx_contrib_coop_es = Column(Float, nullable=False)
    tx_contrib_coop_ea = Column(Float, nullable=False)
    tx_frais_km = Column(Float, nullable=False)
    tx_tva_1 = Column(Float, nullable=False, server_default=text("'0.196'"))
    tx_tva_2 = Column(Float, nullable=False, server_default=text("'0.055'"))
    tx_provision = Column(Float, nullable=False)
    tx_risque_ch = Column(Float, nullable=False)
    tx_creances_irr = Column(Float, nullable=False)
    doc_logo = Column(String(255), nullable=False)
    doc_entete = Column(String(255), nullable=False)
    doc_reglement = Column(String(255), nullable=False)
    doc_charte_act = Column(String(255), nullable=False)
    doc_charte_emploi = Column(String(255), nullable=False)
    doc_cgv = Column(String(255), nullable=False)
    user_compta = Column(String(255), nullable=False)
    pass_compta = Column(String(255), nullable=False)
    tx_smic = Column(Float, nullable=False)
    code_journal_achats = Column(String(6), nullable=False)
    code_journal_frais = Column(String(6), nullable=False)
    code_journal_ventes = Column(String(6), nullable=False)
    liste_depts = Column(String(255), nullable=False)
    bloc_dv_1 = Column(Text, nullable=False)
    bloc_dv_2 = Column(Text, nullable=False)
    bloc_fc_1 = Column(Text, nullable=False)
    bloc_fc_2 = Column(Text, nullable=False)
    num_cpta_tvar1 = Column(String(13), nullable=False)
    num_cpta_tvar2 = Column(String(13), nullable=False)
    num_cpta_tvac1 = Column(String(13), nullable=False)
    num_cpta_tvac2 = Column(String(13), nullable=False)
    num_cpta_transfert = Column(String(13), nullable=False)
    num_cpta_interessement = Column(String(13), nullable=False)
    code_journal_ran = Column(String(6), nullable=False)
    code_journal_caisse = Column(String(6), nullable=False)
    sap_agrement = Column(String(255), nullable=False)
    tx_tva_3 = Column(Float, nullable=False)
    tx_tva_4 = Column(Float, nullable=False)
    tx_tva_5 = Column(Float, nullable=False)
    num_cpta_tvar3 = Column(String(13), nullable=False)
    num_cpta_tvar4 = Column(String(13), nullable=False)
    num_cpta_tvar5 = Column(String(13), nullable=False)
    num_cpta_tvac3 = Column(String(13), nullable=False)
    num_cpta_tvac4 = Column(String(13), nullable=False)
    num_cpta_tvac5 = Column(String(13), nullable=False)
    aff_entetes = Column(String(255), nullable=False, server_default=text("'Complet'"))
    doc_logos_presences = Column(String(255), nullable=False)
    grp_achats = Column(Integer, nullable=False)
    grp_frais = Column(Integer, nullable=False)
    num_cpta_clients_tva1 = Column(String(13), nullable=False)
    num_cpta_clients_tva2 = Column(String(13), nullable=False)
    num_cpta_clients_tva3 = Column(String(13), nullable=False)
    num_cpta_clients_tva4 = Column(String(13), nullable=False)
    num_cpta_clients_tva5 = Column(String(13), nullable=False)
    num_cpta_clients_tvaexo = Column(String(13), nullable=False)
    num_cpta_clients_tiers = Column(String(17), nullable=False)
    pied_page = Column(Text, nullable=False)
    num_folio = Column(String(3), nullable=False, server_default=text("'000'"))
    tx_tva_6 = Column(Float, nullable=False)
    tx_tva_7 = Column(Float, nullable=False)
    num_cpta_tvar6 = Column(String(13), nullable=False)
    num_cpta_tvar7 = Column(String(13), nullable=False)
    num_cpta_tvac6 = Column(String(13), nullable=False)
    num_cpta_tvac7 = Column(String(13), nullable=False)
    num_cpta_clients_tva6 = Column(String(13), nullable=False)
    num_cpta_clients_tva7 = Column(String(13), nullable=False)
    grp_remises = Column(Integer, nullable=False)


t_cooperative_infos = Table(
    'cooperative_infos', metadata,
    Column('formation_1', Integer, nullable=False),
    Column('formation_2', Integer, nullable=False),
    Column('formation_3', Integer, nullable=False),
    Column('formation_4', Integer, nullable=False),
    Column('formation_5', Integer, nullable=False),
    Column('formation_6', Integer, nullable=False),
    Column('formation_7', Integer, nullable=False),
    Column('prevoyance_1', Integer, nullable=False),
    Column('complementaire_1', Integer, nullable=False),
    Column('complementaire_2', Integer, nullable=False),
    Column('complementaire_3', Integer, nullable=False),
    Column('complementaire_4', Integer, nullable=False),
    Column('complementaire_5', Integer, nullable=False),
    Column('complementaire_6', Integer, nullable=False),
    Column('syndic_1', Integer, nullable=False),
    Column('syndic_2', Integer, nullable=False),
    Column('syndic_3', Integer, nullable=False),
    Column('syndic_4', Integer, nullable=False),
    Column('adhesion_1', Integer, nullable=False),
    Column('adhesion_2', Text, nullable=False),
    Column('parts_locaux_1', Text, nullable=False)
)


class CooperativeRib(BASE):
    __tablename__ = 'cooperative_rib'

    banque = Column(String(255), nullable=False)
    etablissement = Column(String(5), nullable=False)
    guichet = Column(String(5), nullable=False)
    num_compte = Column(String(11), primary_key=True)
    cle = Column(String(2), nullable=False)
    defaut = Column(Integer, nullable=False)
    num_cpta_banque = Column(String(13), nullable=False)
    code_journal = Column(String(6), nullable=False)
    iban = Column(String(35), nullable=False)
    bic = Column(String(15), nullable=False)


class Cotisation(BASE):
    __tablename__ = 'cotisations'

    id_cotisation = Column(Integer, primary_key=True)
    id_base = Column(Integer, nullable=False, server_default=text("'0'"))
    nom = Column(String(50), nullable=False, server_default=text("''"))
    taux_sal = Column(Float, nullable=False, server_default=text("'0'"))
    taux_pat = Column(Float, nullable=False, server_default=text("'0'"))
    liste_mois = Column(String(255), nullable=False, server_default=text("''"))
    plafone = Column(Integer, nullable=False, server_default=text("'0'"))
    non_imposable = Column(Integer, nullable=False, server_default=text("'0'"))
    taux_sal_trb = Column(Float, nullable=False, server_default=text("'0'"))
    taux_pat_trb = Column(Float, nullable=False, server_default=text("'0'"))
    id_type_cotis = Column(Integer, nullable=False, server_default=text("'0'"))
    spe = Column(String(2), nullable=False, server_default=text("'NA'"))


class CotisationsDefaut(BASE):
    __tablename__ = 'cotisations_defaut'

    ordre = Column(Integer, primary_key=True)
    id_cotis = Column(Integer, nullable=False)


class Devi(BASE):
    __tablename__ = 'devis'

    id_devis = Column(String(30), primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    date_devis = Column(Date, nullable=False, index=True, server_default=text("'0000-00-00'"))
    total_ttc = Column(Numeric(16, 4), nullable=False)
    tva = Column(Float, nullable=False, server_default=text("'0'"))
    methode = Column(Integer, nullable=False, server_default=text("'1'"))
    coefficient = Column(Float, nullable=False, server_default=text("'0'"))
    marge = Column(Float, nullable=False, server_default=text("'0'"))
    aleas = Column(Float, nullable=False, server_default=text("'0'"))
    risque = Column(Float, nullable=False, server_default=text("'0'"))
    valide = Column(Integer, nullable=False, server_default=text("'0'"))
    signe = Column(Integer, nullable=False, server_default=text("'0'"))
    acompte = Column(Float, nullable=False, server_default=text("'0'"))
    commentaire = Column(Text, nullable=False)
    contrib_cae = Column(Float, nullable=False, server_default=text("'0.1'"))
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)
    etat = Column(String(255), nullable=False)
    delai_reglement = Column(Integer, nullable=False)


class DevisCritere(BASE):
    __tablename__ = 'devis_criteres'

    id_devis = Column(String(255), primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    num_critere = Column(Integer, primary_key=True, nullable=False)
    libelle = Column(String(255), nullable=False)
    valeur = Column(String(255), nullable=False)


class DevisInfo(BASE):
    __tablename__ = 'devis_infos'

    id_devis = Column(String(255), primary_key=True)
    cae_nom = Column(String(255), nullable=False)
    cae_forme_juridique = Column(String(255), nullable=False)
    cae_adresse = Column(String(255), nullable=False)
    cae_adresse_s = Column(String(255), nullable=False)
    cae_cp = Column(String(5), nullable=False)
    cae_ville = Column(String(255), nullable=False)
    cae_tel = Column(String(18), nullable=False)
    cae_fax = Column(String(18), nullable=False)
    cae_mail = Column(String(255), nullable=False)
    cae_num_siret = Column(String(17), nullable=False)
    cae_code_ape = Column(String(5), nullable=False)
    cae_num_tvaintra = Column(String(255), nullable=False)
    cae_mode_fact = Column(String(255), nullable=False)
    cae_num_sap = Column(String(255), nullable=False)
    cae_aff_entetes = Column(String(255), nullable=False)
    pp_entreprise = Column(String(255), nullable=False)
    pp_nom = Column(String(255), nullable=False)
    pp_prenom = Column(String(255), nullable=False)
    pp_adresse = Column(String(255), nullable=False)
    pp_cp = Column(String(5), nullable=False)
    pp_ville = Column(String(255), nullable=False)
    pp_tel = Column(String(18), nullable=False)
    pp_port = Column(String(18), nullable=False)
    pp_fax = Column(String(18), nullable=False)
    pp_mail = Column(String(255), nullable=False)
    pp_num_imm = Column(String(255), nullable=False)
    pp_logo = Column(String(255), nullable=False)
    client_rs = Column(String(255), nullable=False)
    client_civilite = Column(String(255), nullable=False)
    client_nom = Column(String(255), nullable=False)
    client_prenom = Column(String(255), nullable=False)
    client_adresse = Column(String(255), nullable=False)
    client_adresse_s = Column(String(255), nullable=False)
    client_cp = Column(String(5), nullable=False)
    client_ville = Column(String(255), nullable=False)
    client_num_tvaintra = Column(String(255), nullable=False)
    client_cpta_411 = Column(String(13), nullable=False)
    client_cpta_411_tiers = Column(String(13), nullable=False)
    mo_rs = Column(String(255), nullable=False)
    mo_adresse = Column(String(255), nullable=False)
    mo_cp = Column(String(5), nullable=False)
    mo_ville = Column(String(255), nullable=False)
    rib_banque = Column(String(255), nullable=False)
    rib_etabl = Column(String(5), nullable=False)
    rib_guichet = Column(String(5), nullable=False)
    rib_num_compte = Column(String(11), nullable=False)
    rib_cle = Column(String(2), nullable=False)
    rib_iban = Column(String(35), nullable=False)
    rib_bic = Column(String(15), nullable=False)
    bloc_1 = Column(Text, nullable=False)
    bloc_2 = Column(Text, nullable=False)
    mode_fact = Column(String(255), nullable=False)
    mask_entete = Column(Integer, nullable=False)
    sa_no_tva = Column(Integer, nullable=False)
    client_pays = Column(String(255), nullable=False, server_default=text("'FRANCE'"))
    pp_site_web = Column(String(255), nullable=False)
    cae_pied_page = Column(Text, nullable=False)


class DevisLigne(BASE):
    __tablename__ = 'devis_lignes'

    id_devis = Column(String(30), primary_key=True, nullable=False)
    code = Column(String(255), primary_key=True, nullable=False)
    designation = Column(String(255), nullable=False)
    unite = Column(String(30), nullable=False)
    tva = Column(Float, nullable=False)
    prix_ht = Column(Numeric(16, 4), nullable=False)
    qt = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    indice = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)


class DocsFusion(BASE):
    __tablename__ = 'docs_fusion'

    id_doc_fusion = Column(Integer, primary_key=True)
    nom = Column(String(255), nullable=False)
    modele = Column(String(255), nullable=False)
    liaison_event = Column(Integer, nullable=False)
    permanents = Column(Integer, nullable=False)


class DocsFusionDetail(BASE):
    __tablename__ = 'docs_fusion_detail'

    id_doc_fusion = Column(Integer, primary_key=True, nullable=False)
    marqueur = Column(String(255), primary_key=True, nullable=False)
    provenance = Column(String(255), nullable=False)
    element = Column(String(255), nullable=False)
    bdd = Column(String(255), nullable=False)


class Document(BASE):
    __tablename__ = 'documents'

    id_doc = Column(Integer, primary_key=True)
    id_porteur = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    nom = Column(String(255), nullable=False)
    libelle = Column(String(255), nullable=False)
    id_parcours = Column(Integer, nullable=False)


class Droit(BASE):
    __tablename__ = 'droits'

    user = Column(Integer, primary_key=True, nullable=False)
    droit = Column(String(255), primary_key=True, nullable=False)


class Echeancier(BASE):
    __tablename__ = 'echeanciers'

    id_devis = Column(String(30), primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    indice = Column(Integer, primary_key=True, nullable=False)
    libelle = Column(String(255), nullable=False)
    montant = Column(Float, nullable=False)


class EdpCritere(BASE):
    __tablename__ = 'edp_criteres'

    id_edp = Column(Integer, primary_key=True, nullable=False)
    id_chantier = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    num_critere = Column(Integer, primary_key=True, nullable=False)
    libelle = Column(String(255), nullable=False)
    valeur = Column(String(255), nullable=False)


class Encaissement(BASE):
    __tablename__ = 'encaissements'

    id_encaissement = Column(Integer, primary_key=True)
    id_porteur = Column(Integer, nullable=False, server_default=text("'0'"))
    id_facture = Column(String(30), nullable=False, server_default=text("'0'"))
    id_client = Column(Integer, nullable=False)
    date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    montant_ttc = Column(Numeric(16, 4), nullable=False)
    moyen_paiement = Column(Integer, nullable=False, server_default=text("'0'"))
    num_cheque = Column(Integer, nullable=False, server_default=text("'0'"))
    banque_cheque = Column(Integer, nullable=False, server_default=text("'0'"))
    nom_cheque = Column(String(255), nullable=False, server_default=text("''"))
    num_cpta_journal = Column(String(13), nullable=False)
    num_cpta_banque = Column(String(13), nullable=False)
    date_export = Column(Date, nullable=False, index=True)
    verrouille = Column(Integer, nullable=False)
    num_remise = Column(String(255), nullable=False, index=True)


class Entreprise(BASE):
    __tablename__ = 'entreprise'

    id_porteur = Column(Integer, primary_key=True, server_default=text("'0'"))
    nom_entreprise = Column(String(50), nullable=False, server_default=text("''"))
    nom_porteur = Column(String(50), nullable=False, server_default=text("''"))
    adresse = Column(String(255), nullable=False, server_default=text("''"))
    cp = Column(String(5), nullable=False, server_default=text("''"))
    ville = Column(String(50), nullable=False, server_default=text("''"))
    tel = Column(String(14), nullable=False, server_default=text("''"))
    fax = Column(String(14), nullable=False, server_default=text("''"))
    port = Column(String(14), nullable=False)
    mail = Column(String(255), nullable=False, server_default=text("''"))
    logo = Column(String(255), nullable=False)
    mode_facturation = Column(String(255), nullable=False, server_default=text("'Classique'"))
    recap_ventes = Column(Integer, nullable=False)
    coef_charges = Column(Float, nullable=False, server_default=text("'0'"))
    coef_cae = Column(Float, nullable=False, server_default=text("'0'"))
    accompte = Column(Float, nullable=False, server_default=text("'30'"))
    taux_h = Column(Float, nullable=False, server_default=text("'0'"))
    marge = Column(Float, nullable=False, server_default=text("'0'"))
    taux_km = Column(Float, nullable=False, server_default=text("'0'"))
    num_cpta_clients = Column(String(13), nullable=False)
    num_cpta_clients2 = Column(String(13), nullable=False)
    num_cpta_clients3 = Column(String(13), nullable=False)
    num_cpta_clients_tiers = Column(String(17), nullable=False)
    montant_val = Column(Float, nullable=False)
    mask_entete = Column(Integer, nullable=False)
    rib_cae = Column(String(11), nullable=False)
    num_cpta_tvar1 = Column(String(13), nullable=False)
    num_cpta_tvar2 = Column(String(13), nullable=False)
    num_cpta_tvac1 = Column(String(13), nullable=False)
    num_cpta_tvac2 = Column(String(13), nullable=False)
    num_immatriculation = Column(String(255), nullable=False)
    num_cpta_tvar3 = Column(String(13), nullable=False)
    num_cpta_tvar4 = Column(String(13), nullable=False)
    num_cpta_tvar5 = Column(String(13), nullable=False)
    num_cpta_tvac3 = Column(String(13), nullable=False)
    num_cpta_tvac4 = Column(String(13), nullable=False)
    num_cpta_tvac5 = Column(String(13))
    num_cpta_clients_3 = Column(String(13), nullable=False)
    num_cpta_clients_4 = Column(String(13), nullable=False)
    num_cpta_clients_5 = Column(String(13), nullable=False)
    montant_val_fc = Column(Float, nullable=False)
    delai_reglement = Column(Integer, nullable=False)
    site_web = Column(String(255), nullable=False)
    fact_simple = Column(Integer, nullable=False)
    num_cpta_tvar6 = Column(String(13), nullable=False)
    num_cpta_tvar7 = Column(String(13), nullable=False)
    num_cpta_tvac6 = Column(String(13), nullable=False)
    num_cpta_tvac7 = Column(String(13), nullable=False)
    num_cpta_clients_6 = Column(String(13), nullable=False)
    num_cpta_clients_7 = Column(String(13), nullable=False)


class EntrepriseRsa(BASE):
    __tablename__ = 'entreprise_rsa'

    id_porteur = Column(Integer, primary_key=True)
    date_creation = Column(Date, nullable=False)
    statut = Column(String(255), nullable=False)
    activite = Column(String(255), nullable=False)
    num_siret = Column(String(255), nullable=False)
    capital = Column(Numeric(9, 2), nullable=False)
    nb_salaries = Column(Integer, nullable=False)
    statut_dirigeant = Column(String(255), nullable=False)
    zone_prioritaire = Column(String(255), nullable=False)
    centre_enregistrement = Column(String(255), nullable=False)
    local_type = Column(String(255), nullable=False)
    local_etat = Column(String(255), nullable=False)
    local_resultat = Column(String(255), nullable=False)
    local_superficie = Column(Integer, nullable=False)


class EtudeDePrix(BASE):
    __tablename__ = 'etude_de_prix'

    id_etude = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_chantier2 = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    nom_etude = Column(String(255), nullable=False, server_default=text("''"))
    date_etude = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    coefficient = Column(Float, nullable=False, server_default=text("'0'"))
    tva = Column(Float, nullable=False, server_default=text("'0'"))
    montant_ttc = Column(Numeric(16, 4), nullable=False)
    methode = Column(Integer, nullable=False, server_default=text("'1'"))
    marge = Column(Float, nullable=False, server_default=text("'0'"))
    aleas = Column(Float, nullable=False, server_default=text("'0'"))
    risque = Column(Float, nullable=False, server_default=text("'0'"))
    signe = Column(Integer, nullable=False, server_default=text("'0'"))
    contrib_cae = Column(Float, nullable=False, server_default=text("'0.1'"))
    commentaire = Column(Text, nullable=False)
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)
    delai_reglement = Column(Integer, nullable=False)


class Evenement(BASE):
    __tablename__ = 'evenements'

    id_event = Column(Integer, primary_key=True)
    libelle = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False, index=True)
    statut_ass = Column(String(255), nullable=False, index=True)
    position_ass = Column(String(255), nullable=False)
    frequence = Column(Integer, nullable=False)
    type_frequence = Column(String(255), nullable=False)
    conditions = Column(Text, nullable=False)
    consequences = Column(Text, nullable=False)
    is_ct = Column(Integer, nullable=False)
    is_sortie = Column(Integer, nullable=False)
    is_reunion_info = Column(Integer, nullable=False)


class EvenementsDoc(BASE):
    __tablename__ = 'evenements_docs'

    id_event = Column(Integer, primary_key=True, nullable=False)
    id_doc_fusion = Column(Integer, primary_key=True, nullable=False)


class Facture(BASE):
    __tablename__ = 'factures'

    id_facture = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_chantier = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_devis = Column(String(30), nullable=False, index=True)
    date_facture = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    total_ttc = Column(Numeric(16, 4), nullable=False)
    tva = Column(Float, nullable=False, server_default=text("'0'"))
    methode = Column(Integer, nullable=False, server_default=text("'1'"))
    coefficient = Column(Float, nullable=False, server_default=text("'0'"))
    marge = Column(Float, nullable=False, server_default=text("'0'"))
    aleas = Column(Float, nullable=False, server_default=text("'0'"))
    risque = Column(Float, nullable=False, server_default=text("'0'"))
    contrib_cae = Column(Float, nullable=False, server_default=text("'0.1'"))
    mask_devis = Column(Integer, nullable=False)
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)


class FacturesCritere(BASE):
    __tablename__ = 'factures_criteres'

    id_facture = Column(String(255), primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    num_critere = Column(Integer, primary_key=True, nullable=False)
    libelle = Column(String(255), nullable=False)
    valeur = Column(String(255), nullable=False)


class FacturesInfo(BASE):
    __tablename__ = 'factures_infos'

    id_facture = Column(String(255), primary_key=True)
    cae_nom = Column(String(255), nullable=False)
    cae_forme_juridique = Column(String(255), nullable=False)
    cae_adresse = Column(String(255), nullable=False)
    cae_adresse_s = Column(String(255), nullable=False)
    cae_cp = Column(String(5), nullable=False)
    cae_ville = Column(String(255), nullable=False)
    cae_tel = Column(String(18), nullable=False)
    cae_fax = Column(String(18), nullable=False)
    cae_mail = Column(String(255), nullable=False)
    cae_num_siret = Column(String(17), nullable=False)
    cae_code_ape = Column(String(5), nullable=False)
    cae_num_tvaintra = Column(String(255), nullable=False)
    cae_mode_fact = Column(String(255), nullable=False)
    cae_num_sap = Column(String(255), nullable=False)
    cae_aff_entetes = Column(String(255), nullable=False)
    pp_entreprise = Column(String(255), nullable=False)
    pp_nom = Column(String(255), nullable=False)
    pp_prenom = Column(String(255), nullable=False)
    pp_adresse = Column(String(255), nullable=False)
    pp_cp = Column(String(5), nullable=False)
    pp_ville = Column(String(255), nullable=False)
    pp_tel = Column(String(18), nullable=False)
    pp_port = Column(String(18), nullable=False)
    pp_fax = Column(String(18), nullable=False)
    pp_mail = Column(String(255), nullable=False)
    pp_num_imm = Column(String(255), nullable=False)
    pp_logo = Column(String(255), nullable=False)
    client_rs = Column(String(255), nullable=False)
    client_civilite = Column(String(255), nullable=False)
    client_nom = Column(String(255), nullable=False)
    client_prenom = Column(String(255), nullable=False)
    client_adresse = Column(String(255), nullable=False)
    client_adresse_s = Column(String(255), nullable=False)
    client_cp = Column(String(5), nullable=False)
    client_ville = Column(String(255), nullable=False)
    client_num_tvaintra = Column(String(255), nullable=False)
    client_cpta_411 = Column(String(13), nullable=False)
    client_cpta_411_tiers = Column(String(13), nullable=False)
    mo_rs = Column(String(255), nullable=False)
    mo_adresse = Column(String(255), nullable=False)
    mo_cp = Column(String(5), nullable=False)
    mo_ville = Column(String(255), nullable=False)
    rib_banque = Column(String(255), nullable=False)
    rib_etabl = Column(String(5), nullable=False)
    rib_guichet = Column(String(5), nullable=False)
    rib_num_compte = Column(String(11), nullable=False)
    rib_cle = Column(String(2), nullable=False)
    rib_iban = Column(String(35), nullable=False)
    rib_bic = Column(String(15), nullable=False)
    bloc_1 = Column(Text, nullable=False)
    bloc_2 = Column(Text, nullable=False)
    mode_fact = Column(String(255), nullable=False)
    mask_entete = Column(Integer, nullable=False)
    sa_no_tva = Column(Integer, nullable=False)
    client_pays = Column(String(255), nullable=False, server_default=text("'FRANCE'"))
    pp_site_web = Column(String(255), nullable=False)
    cae_pied_page = Column(Text, nullable=False)


class FacturesLigne(BASE):
    __tablename__ = 'factures_lignes'

    id_facture = Column(String(30), primary_key=True, nullable=False)
    code = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)
    unite = Column(String(30), nullable=False)
    tva = Column(Float, nullable=False)
    prix_ht = Column(Numeric(16, 4), nullable=False)
    qt = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    indice = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)


class Famille(BASE):
    __tablename__ = 'famille'

    id_famille = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    nom_famille = Column(String(50), nullable=False, server_default=text("''"))


class Fournisseur(BASE):
    __tablename__ = 'fournisseurs'

    id_fournisseur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    raison_sociale = Column(String(100), nullable=False, server_default=text("''"))
    adresse = Column(String(255), nullable=False, server_default=text("''"))
    adresse_s = Column(String(255), nullable=False, server_default=text("''"))
    cp = Column(String(6), nullable=False, server_default=text("''"))
    ville = Column(String(255), nullable=False, server_default=text("''"))
    mail = Column(String(255), nullable=False, server_default=text("''"))
    tel = Column(String(14), nullable=False, server_default=text("''"))
    fax = Column(String(14), nullable=False, server_default=text("''"))
    site = Column(String(255), nullable=False, server_default=text("''"))
    nom_contact = Column(String(100), nullable=False, server_default=text("''"))
    type_reg = Column(Integer, nullable=False, server_default=text("'0'"))
    num_cpta_401 = Column(String(13), nullable=False)
    num_cpta_401_tiers = Column(String(17), nullable=False)


class Frai(BASE):
    __tablename__ = 'frais'
    __table_args__ = (
        Index('id_porteur', 'id_porteur', 'mois', 'annee'),
    )

    id_frais = Column(Integer, primary_key=True)
    id_note = Column(Integer, nullable=False)
    id_porteur = Column(Integer, nullable=False)
    mois = Column(Integer, nullable=False)
    annee = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    id_client = Column(Integer, nullable=False)
    id_chantier = Column(Integer, nullable=False)
    num_facture = Column(String(255), nullable=False)
    libelle = Column(Text, nullable=False)
    compte = Column(String(13), nullable=False)
    taux_tva = Column(Float, nullable=False)
    nb_km = Column(Integer, nullable=False)
    montant_ht = Column(Numeric(16, 4), nullable=False)
    paye = Column(Integer, nullable=False)
    valide = Column(Integer, nullable=False)
    date_export = Column(Date, nullable=False, index=True, server_default=text("'0000-00-00'"))
    num_piece = Column(String(255), nullable=False, index=True)
    num_ordre = Column(Integer, nullable=False)


class InfosPaie(BASE):
    __tablename__ = 'infos_paie'

    id_infos_paie = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    nb_h_mens = Column(Float, nullable=False)
    taux_h = Column(Float, nullable=False)
    brut_mens = Column(Float, nullable=False)
    ca_mini_mens = Column(Float, nullable=False)
    smic = Column(Integer, nullable=False)
    mutuelle = Column(Integer, nullable=False)
    id_groupe = Column(Integer, nullable=False)
    ccp = Column(Integer, nullable=False)
    rbs = Column(Integer, nullable=False)
    zone_trajet = Column(Integer, nullable=False)
    code_compta = Column(String(255), nullable=False)
    metier = Column(String(255), nullable=False)
    statut = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    taux_at = Column(Integer, nullable=False)


class Listing(BASE):
    __tablename__ = 'listings'

    id_listing = Column(Integer, primary_key=True)
    id_porteur = Column(Integer, nullable=False)
    id_chantier = Column(Integer, nullable=False)
    id_devis = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    intitule = Column(String(255), nullable=False)
    remarques = Column(Text, nullable=False)
    aff_prix = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    edite = Column(Integer, nullable=False)


class ListingsLigne(BASE):
    __tablename__ = 'listings_lignes'

    id_listing = Column(Integer, primary_key=True, nullable=False)
    id_materiaux = Column(Integer, primary_key=True, nullable=False)
    nom_materiaux = Column(String(255), nullable=False)
    qt = Column(Float, nullable=False)
    unite = Column(String(255), nullable=False)
    prix = Column(Float, nullable=False)
    remarques = Column(String(255), nullable=False)


class Log(BASE):
    __tablename__ = 'log'

    id = Column(Integer, primary_key=True, server_default=text("'0'"))
    nom = Column(String(255), nullable=False)
    login = Column(String(255), nullable=False)
    _pass = Column('pass', String(255), nullable=False)


class MaitresDoeuvre(BASE):
    __tablename__ = 'maitres_doeuvres'

    id_maitre = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    raison_sociale = Column(String(100), nullable=False, server_default=text("''"))
    adresse = Column(String(255), nullable=False, server_default=text("''"))
    adresse_s = Column(String(255), nullable=False, server_default=text("''"))
    cp = Column(String(6), nullable=False, server_default=text("''"))
    ville = Column(String(255), nullable=False, server_default=text("''"))
    tel = Column(String(14), nullable=False, server_default=text("''"))
    fax = Column(String(14), nullable=False, server_default=text("''"))
    mail = Column(String(255), nullable=False, server_default=text("''"))
    site = Column(String(255), nullable=False, server_default=text("''"))
    nom_contact = Column(String(100), nullable=False, server_default=text("''"))


class Materiaux(BASE):
    __tablename__ = 'materiaux'

    id_materiel = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    nom = Column(String(50), nullable=False, server_default=text("''"))
    prix = Column(Numeric(16, 4), nullable=False)
    id_famille = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))


class MultiEmployeur(BASE):
    __tablename__ = 'multi_employeurs'

    num_employeur = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    employeur = Column(Integer, nullable=False)
    nb_h_mens = Column(Float, nullable=False)


class Paiement(BASE):
    __tablename__ = 'paiements'

    id_paiement = Column(String(30), primary_key=True)
    id_facture = Column(Integer, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    id_chantier = Column(Integer, nullable=False, server_default=text("'0'"))
    date = Column(Date, nullable=False, index=True, server_default=text("'0000-00-00'"))
    type = Column(String(50), nullable=False, server_default=text("''"))
    montant_ttc = Column(Numeric(16, 4), nullable=False)
    encaisse = Column(Numeric(16, 4), nullable=False)
    valide = Column(Integer, nullable=False, server_default=text("'0'"))
    commentaire = Column(Text, nullable=False)
    date_export = Column(Date, nullable=False, index=True, server_default=text("'0000-00-00'"))
    acompte = Column(Numeric(16, 4), nullable=False)
    delai_reglement = Column(Integer, nullable=False)


class Pay(BASE):
    __tablename__ = 'paies'

    id_paie = Column(Integer, primary_key=True)
    id_salarie = Column(Integer, nullable=False, server_default=text("'0'"))
    type_salarie = Column(String(255), nullable=False)
    mois = Column(Integer, nullable=False)
    annee = Column(Integer, nullable=False)
    date_deb = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    id_param = Column(Integer, nullable=False)
    id_constantes = Column(Integer, nullable=False)
    id_infos_paie = Column(Integer, nullable=False)
    origine = Column(String(255), nullable=False)
    statut = Column(String(255), nullable=False)
    mode_reglement = Column(String(100), nullable=False, server_default=text("''"))
    commentaires = Column(Text, nullable=False)
    nb_h_base = Column(Float, nullable=False)
    nb_h_total = Column(Float, nullable=False)
    salaire_base = Column(Float, nullable=False, server_default=text("'0'"))
    total_brut = Column(Float, nullable=False, server_default=text("'0'"))
    charges_sal = Column(Float, nullable=False, server_default=text("'0'"))
    charges_pat = Column(Float, nullable=False, server_default=text("'0'"))
    net_imposable = Column(Float, nullable=False, server_default=text("'0'"))
    net_a_payer = Column(Float, nullable=False, server_default=text("'0'"))
    plafond = Column(Float, nullable=False)
    msg_val = Column(Text, nullable=False)


class PaiesLigne(BASE):
    __tablename__ = 'paies_lignes'

    id_paie = Column(Integer, primary_key=True, nullable=False)
    id_ligne = Column(Integer, primary_key=True, nullable=False)
    type_ligne = Column(String(255), nullable=False)
    reference = Column(Integer, nullable=False)
    libelle = Column(String(255), nullable=False)
    base = Column(Float, nullable=False)
    taux_sal = Column(Float, nullable=False)
    a_deduire = Column(Float, nullable=False)
    a_payer = Column(Float, nullable=False)
    taux_pat = Column(Float, nullable=False)
    montant_pat = Column(Float, nullable=False)
    imposable = Column(Integer, nullable=False)
    plafonee = Column(Integer, nullable=False)


class ParamBilan(BASE):
    __tablename__ = 'param_bilan'

    CG_NUM = Column(String(13), primary_key=True, index=True, server_default=text("''"))
    CG_INTITULE = Column(String(35))
    SECTION = Column(String(1))
    MONTANT = Column(String(1))
    CONDITION = Column(String(1))
    OPERATION = Column(String(1))
    LIEN = Column(Integer)
    COLONNE = Column(String(50))


t_param_codif = Table(
    'param_codif', metadata,
    Column(u'Catégorie', String(50)),
    Column('Code_Param', String(50)),
    Column(u'Libellé_Param', String(50)),
    Index('Main_Index', u'Catégorie', 'Code_Param')
)


class ParamCr(BASE):
    __tablename__ = 'param_cr'

    CG_NUM = Column(String(13), primary_key=True, index=True, server_default=text("''"))
    CG_INTITULE = Column(String(35))
    SECTION = Column(String(1))
    MONTANT = Column(String(1))
    CONDITION = Column(String(1))
    OPERATION = Column(String(1))
    LIEN = Column(Integer)
    GROUPE = Column(String(5))
    CG_ENTREP = Column(Integer)


class ParamFcpta(BASE):
    __tablename__ = 'param_fcpta'

    CG_NUM = Column(String(13), primary_key=True, index=True, server_default=text("''"))
    CG_INTITULE = Column(String(35))
    CLASSE = Column(String(1))
    VENTILATION = Column(Integer)
    INTITULE = Column(String(50))


class ParamFusion(BASE):
    __tablename__ = 'param_fusion'

    provenance = Column(String(255), primary_key=True, nullable=False)
    element = Column(String(255), primary_key=True, nullable=False)
    bdd = Column(String(255), nullable=False)


class ParamIntitule(BASE):
    __tablename__ = 'param_intitules'

    P_GROUPE = Column(Integer, primary_key=True, unique=True, server_default=text("'0'"))
    P_INTI = Column(String(50))


class ParamPay(BASE):
    __tablename__ = 'param_paies'

    id_param_paies = Column(Integer, primary_key=True)
    jours_ouvres = Column(String(255), nullable=False)
    mode_reglement = Column(String(255), nullable=False)
    taux_at_1 = Column(Float, nullable=False)
    taux_at_2 = Column(Float, nullable=False)
    taux_at_3 = Column(Float, nullable=False)


class ParamPaiesEtat(BASE):
    __tablename__ = 'param_paies_etats'

    id_param_etats = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    urssaf_deplafonnee = Column(Float, nullable=False)
    urssaf_plafonnee = Column(Float, nullable=False)
    urssaf_prevoyance = Column(Float, nullable=False)
    urssaf_fnal = Column(Float, nullable=False)
    urssaf_csg = Column(Float, nullable=False)
    urssaf_transport = Column(Float, nullable=False)
    probtp_m1 = Column(Float, nullable=False)
    probtp_m2 = Column(Float, nullable=False)
    probtp_m3 = Column(Float, nullable=False)
    probtp_m4 = Column(Float, nullable=False)
    probtp_m5 = Column(Float, nullable=False)
    probtp_t1 = Column(Float, nullable=False)
    probtp_t2 = Column(Float, nullable=False)
    probtp_t3 = Column(Float, nullable=False)
    probtp_t4 = Column(Float, nullable=False)
    probtp_t5 = Column(Float, nullable=False)
    probtp_t6 = Column(Float, nullable=False)
    probtp_t7 = Column(Float, nullable=False)
    probtp_t8 = Column(Float, nullable=False)
    probtp_t9 = Column(Float, nullable=False)
    probtp_t10 = Column(Float, nullable=False)
    probtp_t11 = Column(Float, nullable=False)
    probtp_t12 = Column(Float, nullable=False)
    probtp_t13 = Column(Float, nullable=False)
    scop = Column(Float, nullable=False)
    union_sociale = Column(Float, nullable=False)
    pole_emploi_1 = Column(Float, nullable=False)
    pole_emploi_2 = Column(Float, nullable=False)
    pole_emploi_3 = Column(Float, nullable=False)
    cibtp_coef_1 = Column(Float, nullable=False)
    cibtp_coef_2 = Column(Float, nullable=False)
    cibtp_coef_3 = Column(Float, nullable=False)
    cibtp_coef_4 = Column(Float, nullable=False)
    cibtp_tx_1 = Column(Float, nullable=False)
    cibtp_tx_2 = Column(Float, nullable=False)
    cibtp_tx_3 = Column(Float, nullable=False)
    cibtp_tx_4 = Column(Float, nullable=False)
    cibtp_tx_5 = Column(Float, nullable=False)
    cibtp_tx_6 = Column(Float, nullable=False)
    tx_medecine_travail = Column(Float, nullable=False)
    coef_medecine_travail = Column(Float, nullable=False)


class ParamTb(BASE):
    __tablename__ = 'param_tb'

    CG_NUM = Column(String(13), primary_key=True, index=True, server_default=text("''"))
    CG_INTITULE = Column(String(35))
    SECTION = Column(String(1))
    MONTANT = Column(String(1))
    CONDITION = Column(String(1))
    OPERATION = Column(String(1))
    LIEN = Column(Integer)
    GROUPE = Column(String(5))


t_param_tiers = Table(
    'param_tiers', metadata,
    Column('CT_NUM', String(17), nullable=False, index=True),
    Column('CT_INTITULE', String(35), nullable=False),
    Column('CG_NUMPRINC', String(13), nullable=False)
)


t_param_treso = Table(
    'param_treso', metadata,
    Column('R_PARTIE', String(1)),
    Column('R_CODE', Integer),
    Column('R_INTITULE', String(50)),
    Column('R_OPERATION', String(1)),
    Column('R_RUBRIQUE', Integer),
    Column('R_SIGNE', String(1)),
    Column('R_CONDITION', String(1)),
    Index('MainIndex', 'R_PARTIE', 'R_CODE', 'R_RUBRIQUE')
)


class Parcour(BASE):
    __tablename__ = 'parcours'

    id_parcours = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    id_event = Column(Integer, nullable=False)
    id_permanent = Column(Integer, nullable=False)
    id_permanence = Column(String(255), nullable=False)
    date_deb = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    heure_deb = Column(Time, nullable=False)
    heure_fin = Column(Time, nullable=False)
    resume = Column(String(255), nullable=False)
    objet = Column(Text, nullable=False)
    bilan = Column(Text, nullable=False)
    presence = Column(Integer, nullable=False, server_default=text("'1'"))
    id_planning = Column(Integer, nullable=False, index=True)
    id_infos_ct = Column(Integer, nullable=False)
    id_infos_sortie = Column(Integer, nullable=False)
    frequence = Column(Integer, nullable=False)
    type_frequence = Column(String(255), nullable=False)
    horde_id = Column(String(255), nullable=False)
    horde_id_perm = Column(String(255), nullable=False)
    prive = Column(Integer, nullable=False)
    phase = Column(String(255), nullable=False)


class ParcoursOrientation(BASE):
    __tablename__ = 'parcours_orientation'

    id_parcours = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    id_acteur = Column(Integer, primary_key=True, nullable=False)


class Permanence(BASE):
    __tablename__ = 'permanences'

    permanence = Column(String(255), primary_key=True)
    complement = Column(String(255), nullable=False)
    adresse = Column(String(255), nullable=False)
    adresse_suite = Column(String(255), nullable=False)
    cp = Column(String(5), nullable=False)
    ville = Column(String(255), nullable=False)
    tel = Column(String(18), nullable=False)
    fax = Column(String(18), nullable=False)
    mail = Column(String(255), nullable=False)


class Permanent(BASE):
    __tablename__ = 'permanents'

    id_permanent = Column(Integer, primary_key=True)
    civilite = Column(String(255), nullable=False)
    nom = Column(String(255), nullable=False)
    prenom = Column(String(255), nullable=False)
    initiales = Column(String(4), nullable=False)
    adresse = Column(String(255), nullable=False)
    adresse_suite = Column(String(255), nullable=False)
    cp = Column(String(5), nullable=False)
    ville = Column(String(255), nullable=False)
    tel = Column(String(18), nullable=False)
    port = Column(String(18), nullable=False)
    mail = Column(String(255), nullable=False)
    date_entree = Column(Date, nullable=False)
    date_sortie = Column(Date, nullable=False)
    is_referent = Column(Integer, nullable=False)
    login = Column(String(255), nullable=False)
    _pass = Column('pass', String(255), nullable=False)
    num_secu = Column(String(255), nullable=False)
    fonction = Column(String(255), nullable=False)


class PermanentsDoc(BASE):
    __tablename__ = 'permanents_docs'

    id_doc = Column(Integer, primary_key=True)
    id_permanent = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    nom = Column(String(255), nullable=False)
    libelle = Column(String(255), nullable=False)
    id_parcours = Column(Integer, nullable=False)


class PermanentsPay(BASE):
    __tablename__ = 'permanents_paies'

    id_infos_paie = Column(Integer, primary_key=True, nullable=False)
    id_permanent = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    nb_h_mens = Column(Float, nullable=False)
    taux_h = Column(Float, nullable=False)
    brut_mens = Column(Float, nullable=False)
    smic = Column(Integer, nullable=False)
    mutuelle = Column(Integer, nullable=False)
    id_groupe = Column(Integer, nullable=False)
    ccp = Column(Integer, nullable=False)
    rbs = Column(Integer, nullable=False)
    zone_trajet = Column(Integer, nullable=False)
    code_compta = Column(String(255), nullable=False)
    metier = Column(String(255), nullable=False)
    type_permanent = Column(String(10), nullable=False, server_default=text("'Etam'"))


class PermanentsSorty(BASE):
    __tablename__ = 'permanents_sorties'

    id_permanent = Column(Integer, primary_key=True)
    motif_sortie = Column(String(255), nullable=False)
    detail_sortie = Column(Text, nullable=False)
    date_sortie = Column(Date, nullable=False)
    date_entretien = Column(Date, nullable=False)
    date_signature = Column(Date, nullable=False)
    solde = Column(Float, nullable=False)


class Planning(BASE):
    __tablename__ = 'planning'

    id_planning = Column(Integer, primary_key=True)
    id_event = Column(Integer, nullable=False)
    id_permanent = Column(Integer, nullable=False)
    id_permanence = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    heure_deb = Column(Time, nullable=False)
    heure_fin = Column(Time, nullable=False)
    resume = Column(String(255), nullable=False)
    objet = Column(Text, nullable=False)


class Porteur(BASE):
    __tablename__ = 'porteurs'

    id_porteur = Column(
        Integer,
        primary_key=True,
        info={
            "export": {'label': 'coordonnees_identifiant_interne',}
        }
    )
    id_projet = Column(Integer, nullable=False, server_default=text("'0'"))
    stade = Column(String(1), nullable=False, server_default=text("'C'"))
    position = Column(String(255), nullable=False, server_default=text("'Actif'"))
    statut = Column(
        String(255),
        nullable=False,
        server_default=text("'Candidat'"),
        info={
            "export": {'label': '_situation_situation',}
        }
    )
    referent = Column(Integer, nullable=False, server_default=text("'0'"))
    civilite = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_civilite',}
        }
    )
    nom = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_lastname',}
        }
    )
    nom_jf = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_ladies_lastname',}
        }
    )
    prenom = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_firstname',}
        }
    )
    date_naiss = Column(
        Date,
        nullable=False,
        info={
            "export": {'label': 'coordonnees_birthday',}
        }
    )
    dept_naiss = Column(
        String(3),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_birthplace_zipcode',}
        }
    )
    lieu_naiss = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_birthplace',}
        }
    )
    nationalite = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_nationality',}
        }
    )
    adresse = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_address1',}
        }
    )
    adresse_suite = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_address2'}
        }
    )
    cp = Column(
        String(5),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_zipcode',}
        }
    )
    ville = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_city',}
        }
    )
    quartier = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': "coordonnees_zone",},
        }
    )
    zus = Column(Integer, nullable=False)
    tel_1 = Column(
        String(18),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_tel',}
        }
    )
    tel_2 = Column(String(18), nullable=False)
    tel_port = Column(
        String(18),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_mobile',}
        }
    )
    fax = Column(String(18), nullable=False)
    mail = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_email1',}
        }
    )
    obs = Column(Text, nullable=False)
    num_cpta_frns = Column(String(13), nullable=False)
    num_cpta_frns_tiers = Column(String(17), nullable=False)
    num_cpta_frais = Column(String(13), nullable=False)
    num_cpta_frais_tiers = Column(String(17), nullable=False)
    num_cpta_rbmt_achats = Column(String(13), nullable=False)
    num_cpta_rbmt_achats_tiers = Column(String(17), nullable=False)
    photo = Column(String(255), nullable=False)

#    criteres = relationship(
#        "PorteursCritere",
#        backref='porteur',
#        primaryjoin="PorteursCritere.id_porteur==Porteur.id_porteur",
#        uselist=False,
#        foreignkey="PorteursCritere.id_porteur",
#    )


class PorteursCritere(BASE):
    __tablename__ = 'porteurs_criteres'

    id_porteur = Column(
        Integer,
        primary_key=True,
        info={
            "export": {'label': 'coordonnees_identifiant_interne',}
        }
    )
    critere_1 = Column(String(255), nullable=False)
    critere_2 = Column(String(255), nullable=False)
    critere_3 = Column(String(255), nullable=False)
    critere_4 = Column(String(255), nullable=False)
    critere_5 = Column(String(255), nullable=False)
    critere_6 = Column(Text, nullable=False)
    critere_7 = Column(Integer, nullable=False)
    critere_8 = Column(Integer, nullable=False)
    critere_9 = Column(Integer, nullable=False)
    critere_10 = Column(Integer, nullable=False)
    critere_11 = Column(Integer, nullable=False)
    critere_12 = Column(Text, nullable=False)


class PorteursExp(BASE):
    __tablename__ = 'porteurs_exp'

    id_porteur = Column(
        Integer,
        primary_key=True,
        info={
            "export": {'label': 'coordonnees_identifiant_interne',}
        }
    )
    situation = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': '_statut_social_status',}
        }
        # ex : de1/sal/de/rsa
    )
    situation_detail = Column(
        String(255),
        nullable=False,
    )
    situation_obs = Column(Text, nullable=False)
    provenance_cli = Column(String(255), nullable=False)
    form_init = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_study_level',}
            #ex : Niveau II (Licence / Maitrise)
        }
    )
    detail_form_init = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': 'Domaine',}
            #ex : Technique
        }
    )
    annee_form_init = Column(Integer, nullable=False)
    form_continue = Column(String(255), nullable=False)
    metier = Column(String(255), nullable=False)
    exp = Column(Integer, nullable=False)
    activite_projetee = Column(String(255), nullable=False)
    projet_pro = Column(
        String(255),
        nullable=False,
        # ex : Création, rénovation et réparation de bijoux fantaisie
    )
    competences = Column(Text, nullable=False)


class PorteursInfo(BASE):
    __tablename__ = 'porteurs_infos'

    id_porteur = Column(
        Integer,
        primary_key=True,
        info={
            "export": {'label': 'coordonnees_identifiant_interne',}
        }
    )
    situation_fam = Column(
        String(255),
        nullable=False,
        info={
            "export": {'label': '_coordonnees_family_status'}, # postformatting
        }
    )
    num_secu = Column(
        String(15),
        nullable=False,
        info={
            "export": {'label': 'coordonnees_secu'},
        }
    )
    num_anpe = Column(String(255), nullable=False)
    date_anpe = Column(Date, nullable=False)
    nb_enfants_charge = Column(
        Integer,
        nullable=False,
        info={
            "export": {'label': "coordonnees_children"},
        }
    )
    femme_isolee = Column( #cf formatters
        Integer,
        nullable=False,
    )
    montant_assedic = Column(Float, nullable=False)
    date_fin_assedic = Column(
        Date,
        nullable=False,
        info={
            "export": {'label': "statut_end_rights_date"},
        }
    )
    assistante_sociale = Column(Integer, nullable=False)
    th = Column(Integer, nullable=False)
    rib_etabl = Column(String(5), nullable=False)
    rib_guichet = Column(String(5), nullable=False)
    rib_compte = Column(String(11), nullable=False)
    rib_cle = Column(String(2), nullable=False)
    ass_pro = Column(Integer, nullable=False)
    num_police_assurance = Column(String(255), nullable=False)
    assureur = Column(Integer, nullable=False)
    prescripteur_1 = Column(Integer, nullable=False)
    prescripteur_2 = Column(Integer, nullable=False)
    prescripteur_3 = Column(Integer, nullable=False)
    prescripteur_libre = Column(String(255), nullable=False)
    permanence = Column(String(255), nullable=False)
    is_multiemployeurs = Column(Integer, nullable=False)
    beneficiaire_rsa = Column(Integer, nullable=False)
    ressources = Column(String(255), nullable=False)
    rib_iban = Column(String(33), nullable=False)
    rib_bic = Column(String(11), nullable=False)


class PorteursPj(BASE):
    __tablename__ = 'porteurs_pj'

    id_porteur = Column(
        Integer,
        primary_key=True,
        info={
            "export": {'label': 'coordonnees_identifiant_interne',}
        }
    )
    ass_domicile = Column(Integer, nullable=False)
    ass_vehicule = Column(Integer, nullable=False)
    rmi = Column(Integer, nullable=False)
    assedic = Column(Integer, nullable=False)
    carte_id = Column(Integer, nullable=False)
    carte_secu = Column(Integer, nullable=False)
    cv = Column(Integer, nullable=False)
    anpe = Column(Integer, nullable=False)
    diplome = Column(Integer, nullable=False)
    bulletins = Column(Integer, nullable=False)
    decompte_assedic = Column(Integer, nullable=False)
    ct_insert = Column(Integer, nullable=False)
    carte_grise = Column(Integer, nullable=False)
    exp_pro = Column(Integer, nullable=False)
    photo_id = Column(Integer, nullable=False)
    diplome_mini = Column(Integer, nullable=False)
    exp_mini = Column(Integer, nullable=False)
    permis = Column(Integer, nullable=False)
    rib = Column(Integer, nullable=False)
    passeport = Column(Integer, nullable=False)
    autres = Column(Integer, nullable=False)
    autres_nature = Column(String(255), nullable=False)


class PorteursRsa(BASE):
    __tablename__ = 'porteurs_rsa'

    id_porteur = Column(
        Integer,
        primary_key=True,
        info={
            "export": {'label': 'coordonnees_identifiant_interne',}
        }
    )
    num_rsa = Column(String(255), nullable=False)
    num_cli = Column(String(255), nullable=False)
    situation_rsa = Column(String(255), nullable=False)
    date_pd = Column(Date, nullable=False)
    commentaires = Column(Text, nullable=False)
    actions = Column(Text, nullable=False)
    date_fin_mission = Column(Date, nullable=False)
    phase = Column(String(255), nullable=False)


class Produit(BASE):
    __tablename__ = 'produits'

    code = Column(String(30), primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    designation = Column(String(255), nullable=False)
    categorie = Column(String(255), nullable=False)
    id_famille = Column(Integer, nullable=False)
    id_unite = Column(Integer, nullable=False)
    tx_tva = Column(Float, nullable=False)
    tx_frais = Column(Float, nullable=False)
    tx_marge = Column(Float, nullable=False)
    prix_ht = Column(Numeric(16, 4), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)


class Produits20140218(BASE):
    __tablename__ = 'produits_20140218'

    code = Column(String(30), primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    designation = Column(String(255), nullable=False)
    categorie = Column(String(255), nullable=False)
    id_famille = Column(Integer, nullable=False)
    id_unite = Column(Integer, nullable=False)
    tx_tva = Column(Float, nullable=False)
    tx_frais = Column(Float, nullable=False)
    tx_marge = Column(Float, nullable=False)
    prix_ht = Column(Numeric(16, 4), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)


class Projet(BASE):
    __tablename__ = 'projets'

    id_projet = Column(Integer, primary_key=True)
    date_creation = Column(Date, nullable=False)
    raison_sociale = Column(String(255), nullable=False)
    activite = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    secteur_activite = Column(String(255), nullable=False)
    secteur_geo = Column(String(255), nullable=False)
    zone = Column(String(255), nullable=False)
    obs = Column(Text, nullable=False)
    nc_associations = Column(Integer, nullable=False)
    nc_artisans = Column(Integer, nullable=False)
    nc_commercants = Column(Integer, nullable=False)
    nc_collectivites = Column(Integer, nullable=False)
    nc_entreprises = Column(Integer, nullable=False)
    nc_particuliers = Column(Integer, nullable=False)
    nc_autres = Column(Integer, nullable=False)
    porteur_referent = Column(Integer, nullable=False)
    nature_projet = Column(String(255), nullable=False)


class RecapVente(BASE):
    __tablename__ = 'recap_ventes'

    id = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    mois = Column(Integer, primary_key=True, nullable=False)
    annee = Column(Integer, primary_key=True, nullable=False)
    num_facturier = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    client = Column(String(255), nullable=False)
    prestations = Column(String(255), nullable=False)
    reglement = Column(String(255), nullable=False)
    montant_ht = Column(Numeric(16, 4), nullable=False)
    taux_tva = Column(Float, nullable=False)
    id_facture = Column(String(255), nullable=False)
    categorie = Column(String(255), nullable=False)
    num_cpta_7 = Column(String(13), nullable=False)


class Remise(BASE):
    __tablename__ = 'remises'

    num_remise = Column(String(255), primary_key=True)
    date = Column(Date, nullable=False)
    banque = Column(String(255), nullable=False)
    num_compte = Column(String(255), nullable=False)
    num_cpta_banque = Column(String(13), nullable=False)
    date_export = Column(Date, nullable=False)


class Sortie(BASE):
    __tablename__ = 'sorties'

    id_sortie = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False)
    motif_sortie = Column(String(255), nullable=False)
    detail_sortie = Column(Text, nullable=False)
    date_sortie = Column(Date, nullable=False)
    date_entretien = Column(Date, nullable=False)
    date_signature = Column(Date, nullable=False)
    solde = Column(Float, nullable=False)
    retour = Column(Integer, nullable=False)


class TaxeSalaire(BASE):
    __tablename__ = 'taxe_salaires'

    annee = Column(Integer, primary_key=True, nullable=False)
    mois = Column(Integer, primary_key=True, nullable=False)
    montant = Column(Float, nullable=False)


class TypeReglement(BASE):
    __tablename__ = 'type_reglement'

    id_type_reglement = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False, server_default=text("''"))


class Unite(BASE):
    __tablename__ = 'unite'

    id_unite = Column(Integer, primary_key=True, nullable=False)
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    nom_unite = Column(String(15), nullable=False, server_default=text("''"))


class Uo(BASE):
    __tablename__ = 'uo'

    id_uo = Column(String(15), primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    designation = Column(String(255), nullable=False, server_default=text("''"))
    prix_mo = Column(Numeric(16, 4), nullable=False)
    qt_mo = Column(Float, nullable=False, server_default=text("'0'"))
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    prix_uo = Column(Numeric(16, 4), nullable=False)
    qt_uo = Column(Float, nullable=False, server_default=text("'0'"))
    simple = Column(Integer, nullable=False)


class UoMateriaux(BASE):
    __tablename__ = 'uo_materiaux'

    id_materiel = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    qt_materiel = Column(Float, nullable=False, server_default=text("'0'"))


class UoMaterielAffecte(BASE):
    __tablename__ = 'uo_materiel_affecte'

    id_materiel_a = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    id_uo = Column(String(15), primary_key=True, nullable=False, server_default=text("'0'"))
    id_porteur = Column(String(15), primary_key=True, nullable=False, server_default=text("''"))
    nom_materiel_a = Column(String(50), nullable=False, server_default=text("''"))
    prix_public_unit_a = Column(Numeric(16, 4), nullable=False)
    id_unite = Column(Integer, nullable=False, server_default=text("'0'"))
    quantite_materiel_a = Column(Float, nullable=False, server_default=text("'0'"))


t_wr_param_bilan = Table(
    'wr_param_bilan', metadata,
    Column('CPTE2', String(2)),
    Column('CPTE3', String(3)),
    Column('CPTE4', String(4)),
    Column('CPTE5', String(5)),
    Column('SECTION', String(1)),
    Column('MONTANT', String(1)),
    Column('CONDITION', String(1)),
    Column('OPERATION', String(1)),
    Column('LIEN', Integer),
    Column('P_INTI', String(50)),
    Index('MainIndex', 'CPTE2', 'CPTE3', 'CPTE4', 'CPTE5')
)


t_wr_param_cr = Table(
    'wr_param_cr', metadata,
    Column('CPTE2', String(2)),
    Column('CPTE3', String(3)),
    Column('CPTE4', String(4)),
    Column('CPTE5', String(5)),
    Column('SECTION', String(1)),
    Column('MONTANT', String(1)),
    Column('CONDITION', String(1)),
    Column('OPERATION', String(1)),
    Column('GROUPE', String(50)),
    Column('LIEN', Integer),
    Column('P_INTI', String(50)),
    Index('MainIndex', 'CPTE2', 'CPTE3', 'CPTE4')
)


t_wr_param_fcpta = Table(
    'wr_param_fcpta', metadata,
    Column('CPTE2', String(2)),
    Column('CPTE3', String(3)),
    Column('CPTE4', String(4)),
    Column('CLASSE', String(1)),
    Column('VENTILATION', Integer),
    Column('INTITULE', String(50)),
    Index('MainIndex', 'CPTE2', 'CPTE3', 'CPTE4')
)


t_wr_param_tb = Table(
    'wr_param_tb', metadata,
    Column('CPTE2', String(2)),
    Column('CPTE3', String(3)),
    Column('CPTE4', String(4)),
    Column('SECTION', String(1)),
    Column('MONTANT', String(1)),
    Column('CONDITION', String(1)),
    Column('OPERATION', String(1)),
    Column('GROUPE', String(50)),
    Column('LIEN', Integer),
    Column('P_INTI', String(50)),
    Index('MainIndex', 'CPTE2', 'CPTE3', 'CPTE4')
)

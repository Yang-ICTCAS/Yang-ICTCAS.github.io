---
title: ''
date: 2024-01-01
type: landing

design:
  spacing: '5rem'

sections:
  - block: resume-biography-3
    id: about
    content:
      username: admin
      text: ''
      button:
        text: Google Scholar
        url: https://scholar.google.com/citations?user=EN3zdQ8AAAAJ&hl=en
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: bg-triangles.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false

  - block: markdown
    id: research
    content:
      title: Research Areas
      text: |-
        My research lies at the intersection of **artificial intelligence** and **life sciences**. I aim to build intelligent systems that can understand, simulate, and assist with complex biological and medical tasks.

        **AI for Science / Digital Cell**
        Building large-scale foundation models for single-cell biology, enabling in-silico simulation of cellular behaviors, gene regulatory networks, and cross-species biological analysis.

        **Multimodal Large Models**
        Developing foundation models capable of understanding and integrating heterogeneous data modalities — text, images, omics, and clinical records — for scientific discovery.

        **Smart Healthcare**
        Applying AI to clinical decision support, medical image analysis, and perioperative risk prediction, with a focus on real-world deployability and privacy preservation.

        **Federated Learning**
        Designing privacy-preserving distributed learning algorithms to handle data heterogeneity, label noise, and non-IID distributions across clinical institutions.
    design:
      columns: '1'

  - block: collection
    id: publications
    content:
      title: Selected Publications
      text: ''
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
      columns: '1'

  - block: collection
    id: projects
    content:
      title: Research Projects
      text: ''
      filters:
        folders:
          - project
    design:
      view: card
      columns: '2'

  - block: resume-awards
    id: awards
    content:
      username: admin
    design:
      columns: '1'

  - block: contact
    id: contact
    content:
      title: Contact
      text: ''
      email: yangxiaodong@ict.ac.cn
      address:
        street: No. 6 Kexueyuan South Road, Zhongguancun
        city: Beijing
        postcode: '100190'
        country: China
        country_code: CN
      autolink: true
    design:
      columns: '1'
---

# Lista de 100 números (exemplo)
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = 45, 23, 67, 12, 98, 34, 56, 78, 12, 23
n11, n12, n13, n14, n15, n16, n17, n18, n19, n20 = 45, 67, 89, 34, 56, 78, 90, 12, 34, 56
n21, n22, n23, n24, n25, n26, n27, n28, n29, n30 = 78, 90, 23, 45, 67, 89, 12, 34, 56, 78
n31, n32, n33, n34, n35, n36, n37, n38, n39, n40 = 90, 23, 45, 67, 89, 12, 34, 56, 78, 90
n41, n42, n43, n44, n45, n46, n47, n48, n49, n50 = 23, 45, 67, 89, 12, 34, 56, 78, 90, 23
n51, n52, n53, n54, n55, n56, n57, n58, n59, n60 = 45, 67, 89, 12, 34, 56, 78, 90, 23, 45
n61, n62, n63, n64, n65, n66, n67, n68, n69, n70 = 67, 89, 12, 34, 56, 78, 90, 23, 45, 67
n71, n72, n73, n74, n75, n76, n77, n78, n79, n80 = 89, 12, 34, 56, 78, 90, 23, 45, 67, 89
n81, n82, n83, n84, n85, n86, n87, n88, n89, n90 = 12, 34, 56, 78, 90, 23, 45, 67, 89, 12
n91, n92, n93, n94, n95, n96, n97, n98, n99, n100 = 34, 56, 78, 90, 23, 45, 67, 89, 12, 34

# Ordenando com bubble sort usando if
trocado = True
while trocado:
    trocado = False
    if n1 > n2: n1, n2 = n2, n1; trocado = True
    if n2 > n3: n2, n3 = n3, n2; trocado = True
    if n3 > n4: n3, n4 = n4, n3; trocado = True
    if n4 > n5: n4, n5 = n5, n4; trocado = True
    if n5 > n6: n5, n6 = n6, n5; trocado = True
    if n6 > n7: n6, n7 = n7, n6; trocado = True
    if n7 > n8: n7, n8 = n8, n7; trocado = True
    if n8 > n9: n8, n9 = n9, n8; trocado = True
    if n9 > n10: n9, n10 = n10, n9; trocado = True
    if n10 > n11: n10, n11 = n11, n10; trocado = True
    if n11 > n12: n11, n12 = n12, n11; trocado = True
    if n12 > n13: n12, n13 = n13, n12; trocado = True
    if n13 > n14: n13, n14 = n14, n13; trocado = True
    if n14 > n15: n14, n15 = n15, n14; trocado = True
    if n15 > n16: n15, n16 = n16, n15; trocado = True
    if n16 > n17: n16, n17 = n17, n16; trocado = True
    if n17 > n18: n17, n18 = n18, n17; trocado = True
    if n18 > n19: n18, n19 = n19, n18; trocado = True
    if n19 > n20: n19, n20 = n20, n19; trocado = True
    if n20 > n21: n20, n21 = n21, n20; trocado = True
    if n21 > n22: n21, n22 = n22, n21; trocado = True
    if n22 > n23: n22, n23 = n23, n22; trocado = True
    if n23 > n24: n23, n24 = n24, n23; trocado = True
    if n24 > n25: n24, n25 = n25, n24; trocado = True
    if n25 > n26: n25, n26 = n26, n25; trocado = True
    if n26 > n27: n26, n27 = n27, n26; trocado = True
    if n27 > n28: n27, n28 = n28, n27; trocado = True
    if n28 > n29: n28, n29 = n29, n28; trocado = True
    if n29 > n30: n29, n30 = n30, n29; trocado = True
    if n30 > n31: n30, n31 = n31, n30; trocado = True
    if n31 > n32: n31, n32 = n32, n31; trocado = True
    if n32 > n33: n32, n33 = n33, n32; trocado = True
    if n33 > n34: n33, n34 = n34, n33; trocado = True
    if n34 > n35: n34, n35 = n35, n34; trocado = True
    if n35 > n36: n35, n36 = n36, n35; trocado = True
    if n36 > n37: n36, n37 = n37, n36; trocado = True
    if n37 > n38: n37, n38 = n38, n37; trocado = True
    if n38 > n39: n38, n39 = n39, n38; trocado = True
    if n39 > n40: n39, n40 = n40, n39; trocado = True
    if n40 > n41: n40, n41 = n41, n40; trocado = True
    if n41 > n42: n41, n42 = n42, n41; trocado = True
    if n42 > n43: n42, n43 = n43, n42; trocado = True
    if n43 > n44: n43, n44 = n44, n43; trocado = True
    if n44 > n45: n44, n45 = n45, n44; trocado = True
    if n45 > n46: n45, n46 = n46, n45; trocado = True
    if n46 > n47: n46, n47 = n47, n46; trocado = True
    if n47 > n48: n47, n48 = n48, n47; trocado = True
    if n48 > n49: n48, n49 = n49, n48; trocado = True
    if n49 > n50: n49, n50 = n50, n49; trocado = True
    if n50 > n51: n50, n51 = n51, n50; trocado = True
    if n51 > n52: n51, n52 = n52, n51; trocado = True
    if n52 > n53: n52, n53 = n53, n52; trocado = True
    if n53 > n54: n53, n54 = n54, n53; trocado = True
    if n54 > n55: n54, n55 = n55, n54; trocado = True

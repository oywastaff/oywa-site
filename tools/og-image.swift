// Immagine di anteprima 1200x630 per i social.
// Uso: swift og-image.swift <cartella sito> <file png> <riga1> <riga2> <riga3> <sotto1> <sotto2> <cartella schermate>
import AppKit
import CoreText

let args = CommandLine.arguments
let site = args[1]
let out = args[2]
let W: CGFloat = 1200, H: CGFloat = 630

func color(_ hex: UInt32, _ a: CGFloat = 1) -> NSColor {
    NSColor(srgbRed: CGFloat((hex >> 16) & 0xff) / 255, green: CGFloat((hex >> 8) & 0xff) / 255,
            blue: CGFloat(hex & 0xff) / 255, alpha: a)
}

let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(W), pixelsHigh: Int(H), bitsPerSample: 8,
                           samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
                           bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
let ctx = NSGraphicsContext.current!.cgContext

// Sfondo crema con due macchie morbide.
color(0xFAF3E6).setFill(); ctx.fill(CGRect(x: 0, y: 0, width: W, height: H))
func blob(_ c: NSColor, _ x: CGFloat, _ y: CGFloat, _ r: CGFloat) {
    let g = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(),
                       colors: [c.cgColor, c.withAlphaComponent(0).cgColor] as CFArray, locations: [0, 1])!
    ctx.drawRadialGradient(g, startCenter: CGPoint(x: x, y: y), startRadius: 0,
                           endCenter: CGPoint(x: x, y: y), endRadius: r, options: [])
}
blob(color(0xE8A087, 0.55), 1000, 560, 520)
blob(color(0x7FB8A8, 0.35), 80, 40, 380)

// Telefono con cornice scura e schermata.
func phone(_ file: String, x: CGFloat, y: CGFloat, w: CGFloat, angle: CGFloat) {
    guard let img = NSImage(contentsOfFile: file) else { return }
    let h = w * 2622 / 1206
    ctx.saveGState()
    ctx.translateBy(x: x + w / 2, y: y + h / 2)
    ctx.rotate(by: angle * .pi / 180)
    let frame = CGRect(x: -w / 2, y: -h / 2, width: w, height: h)
    ctx.setShadow(offset: CGSize(width: 0, height: -24), blur: 50, color: color(0x2E2A24, 0.45).cgColor)
    color(0x1C1915).setFill()
    NSBezierPath(roundedRect: frame, xRadius: w * 0.13, yRadius: w * 0.13).fill()
    ctx.setShadow(offset: .zero, blur: 0, color: nil)
    let inset = w * 0.032
    let screen = frame.insetBy(dx: inset, dy: inset)
    let clip = NSBezierPath(roundedRect: screen, xRadius: w * 0.105, yRadius: w * 0.105)
    clip.addClip()
    img.draw(in: screen)
    ctx.restoreGState()
}
phone("\(args[8])/rapido-nome.jpg", x: 700, y: 30, w: 230, angle: 7)
phone("\(args[8])/mappa.jpg", x: 900, y: 70, w: 250, angle: -4)

// Testi.
func text(_ s: String, font: NSFont, color c: NSColor, x: CGFloat, y: CGFloat, width: CGFloat) {
    let p = NSMutableParagraphStyle(); p.lineHeightMultiple = 0.95
    let attr = NSAttributedString(string: s, attributes: [.font: font, .foregroundColor: c, .paragraphStyle: p, .kern: -0.5])
    attr.draw(with: CGRect(x: x, y: y, width: width, height: 400), options: [.usesLineFragmentOrigin])
}
let heavy = NSFont.systemFont(ofSize: 66, weight: .heavy)
let body = NSFont.systemFont(ofSize: 27, weight: .regular)

if let icon = NSImage(contentsOfFile: "\(site)/assets/app_icon.png") {
    ctx.saveGState()
    NSBezierPath(roundedRect: CGRect(x: 72, y: 500, width: 68, height: 68), xRadius: 18, yRadius: 18).addClip()
    icon.draw(in: CGRect(x: 72, y: 500, width: 68, height: 68))
    ctx.restoreGState()
}
NSAttributedString(string: "OYWA", attributes: [.font: NSFont.systemFont(ofSize: 34, weight: .heavy), .foregroundColor: color(0x2E2A24), .kern: 2]).draw(at: CGPoint(x: 158, y: 513))
func line(_ s: String, _ c: NSColor, _ y: CGFloat) {
    NSAttributedString(string: s, attributes: [.font: heavy, .foregroundColor: c, .kern: -1]).draw(at: CGPoint(x: 70, y: y))
}
line(args[3], color(0x2E2A24), 380)
line(args[4], color(0x2E2A24), 306)
line(args[5], color(0xD2785A), 232)
for (i, l) in [args[6], args[7]].enumerated() {
    NSAttributedString(string: l, attributes: [.font: body, .foregroundColor: color(0x6B6258)]).draw(at: CGPoint(x: 72, y: 160 - CGFloat(i) * 38))
}

NSGraphicsContext.restoreGraphicsState()
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: out))

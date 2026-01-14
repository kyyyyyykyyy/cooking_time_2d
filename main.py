# PASTE KODE LENGKAP DARI SINI SAMPAI AKHIR

import pygame
import os
import random
import math

# --- 1. Inisialisasi Pygame dan Pengaturan Awal ---
pygame.init()
pygame.font.init()

# Pengaturan ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cooking Time! (Ultimate Elegance Version)")

# Pengaturan FPS
clock = pygame.time.Clock()

# Definisi Warna
PINK_SOFT = (255, 192, 203)
PURPLE_SOFT = (204, 153, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_LIGHT = (144, 238, 144)
RED_CRITICAL = (255, 99, 71)
TEXT_SHADOW = (100, 100, 100)
UI_PANEL_COLOR = (255, 220, 230, 150)
SPARKLE_COLOR_1 = (255, 182, 193, 100)
SPARKLE_COLOR_2 = (221, 160, 221, 100)
MENU_BUTTON_BG = (180, 140, 220, 180) 
MENU_BUTTON_BORDER = (255, 255, 255, 200) 
SETTINGS_BG_COLOR = (150, 100, 180)
SUNBEAM_COLOR = (255, 255, 200, 20)

# --- 2. Memuat Aset ---
try:
    script_dir = os.path.dirname(__file__)
    ASSET_DIR = os.path.join(script_dir, "assets")
    IMAGE_DIR = os.path.join(ASSET_DIR, "image")
    FONT_DIR = os.path.join(ASSET_DIR, "font")

    BG_GAME = pygame.image.load(os.path.join(IMAGE_DIR, "background_game.png")).convert()
    BG_GAME = pygame.transform.scale(BG_GAME, (SCREEN_WIDTH, SCREEN_HEIGHT))
    try:
        BG_MENU = pygame.image.load(os.path.join(IMAGE_DIR, "background_menu.png")).convert()
        BG_MENU = pygame.transform.scale(BG_MENU, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except FileNotFoundError:
        BG_MENU = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        for y in range(SCREEN_HEIGHT):
            r = int(PINK_SOFT[0] + (PURPLE_SOFT[0] - PINK_SOFT[0]) * (y / SCREEN_HEIGHT))
            g = int(PINK_SOFT[1] + (PURPLE_SOFT[1] - PINK_SOFT[1]) * (y / SCREEN_HEIGHT))
            b = int(PINK_SOFT[2] + (PURPLE_SOFT[2] - PINK_SOFT[2]) * (y / SCREEN_HEIGHT))
            pygame.draw.line(BG_MENU, (r,g,b), (0, y), (SCREEN_WIDTH, y))

    CUTTING_BOARD_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "cutting_board.png")).convert_alpha()
    CUTTING_BOARD_IMG = pygame.transform.scale(CUTTING_BOARD_IMG, (350, 250))
    BOWL_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "bowl.png")).convert_alpha()
    BOWL_IMG = pygame.transform.scale(BOWL_IMG, (180, 140))
    VEGGIE1_FULL_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "vegetable1_full.png")).convert_alpha()
    VEGGIE1_FULL_IMG = pygame.transform.scale(VEGGIE1_FULL_IMG, (150, 60))
    VEGGIE1_SLICE_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "vegetable1_slice.png")).convert_alpha()
    VEGGIE1_SLICE_IMG = pygame.transform.scale(VEGGIE1_SLICE_IMG, (50, 25))
    VEGGIE2_FULL_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "vegetable2_full.png")).convert_alpha()
    VEGGIE2_FULL_IMG = pygame.transform.scale(VEGGIE2_FULL_IMG, (150, 70))
    VEGGIE2_SLICE_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "vegetable2_slice.png")).convert_alpha()
    VEGGIE2_SLICE_IMG = pygame.transform.scale(VEGGIE2_SLICE_IMG, (55, 30))
    KNIFE_IMG = pygame.image.load(os.path.join(IMAGE_DIR, "knife.png")).convert_alpha()
    KNIFE_IMG = pygame.transform.scale(KNIFE_IMG, (80, 30))

    CUSTOM_FONT_PATH = os.path.join(FONT_DIR, "custom_font.ttf")
    FONT_TITLE = pygame.font.Font(CUSTOM_FONT_PATH, 72)
    FONT_BUTTON = pygame.font.Font(CUSTOM_FONT_PATH, 30)
    FONT_FEEDBACK = pygame.font.Font(CUSTOM_FONT_PATH, 48)
    FONT_SMALL = pygame.font.Font(CUSTOM_FONT_PATH, 24)
    FONT_SETTINGS_TITLE = pygame.font.Font(CUSTOM_FONT_PATH, 50) 
    
except pygame.error as e:
    print(f"Error: Tidak bisa memuat aset: {e}"); pygame.quit(); exit()

# --- 3. Variabel Game ---
current_screen = "menu" 
play_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 50, 240, 70) 
settings_button_rect = pygame.Rect(SCREEN_WIDTH - 170, SCREEN_HEIGHT - 60, 160, 50) 
back_button_rect = pygame.Rect(SCREEN_WIDTH - 170, SCREEN_HEIGHT - 60, 160, 50) 

# Mini-game Chopping
# [Variabel Chopping]
cutting_board_rect = CUTTING_BOARD_IMG.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)) 
bowl_rect = BOWL_IMG.get_rect(midleft=(cutting_board_rect.right + 20, cutting_board_rect.centery + 20))
current_veggie_type = "timun"; current_veggie_img = VEGGIE1_FULL_IMG; current_veggie_slice_img = VEGGIE1_SLICE_IMG
current_veggie_rect = current_veggie_img.get_rect(center=cutting_board_rect.center)
current_veggie_cut_count = 0; MAX_CUTS_PER_VEGGIE = 12 
is_dragging_cut = False; cut_start_pos = (0, 0); cut_end_pos = (0, 0); MIN_DRAG_DISTANCE = 30 
score = 0
feedback_data = {"text": "", "color": WHITE, "start_time": 0, "duration": 800, "y_offset": 0, "alpha": 255}
bowl_slices = []
bowl_positions = [(75, 60), (95, 65), (55, 63), (85, 75), (65, 78), (105, 72), (70, 88), (90, 92), (50, 90), (110, 87), (60, 98), (100, 102)]
flying_slices = [] 

# --- 4. Variabel Animasi ---
menu_sparkles = []
for _ in range(20): menu_sparkles.append({"pos": [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)], "radius": random.randint(2, 5), "color": random.choice([SPARKLE_COLOR_1, SPARKLE_COLOR_2]), "life": random.randint(500, 1500), "born": pygame.time.get_ticks()})

# Animasi Sinar Matahari
sunbeam_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
SUNBEAM_ORIGIN = (50, 250) 
NUM_BEAMS = 7
beam_angles = [random.uniform(-0.1, 0.4) for _ in range(NUM_BEAMS)]
beam_alphas = [random.randint(10, 30) for _ in range(NUM_BEAMS)]

# === FUNGSI JUDUL BERDENYUT (DIKEMBALIKAN) ===
def draw_pulsing_text(s, t_surf, sh_surf, c_pos, scale): 
    """Menggambar teks dengan animasi denyut (scaling) dan shadow."""
    # Pastikan scale tidak nol untuk menghindari error
    if scale <= 0: return 
    
    sc_surf = pygame.transform.smoothscale_by(t_surf, scale)
    sc_rect = sc_surf.get_rect(center=c_pos)
    
    sc_sh = pygame.transform.smoothscale_by(sh_surf, scale)
    # Atur posisi shadow sedikit bergeser dari teks utama
    sc_sh_rect = sc_sh.get_rect(center=(c_pos[0] + 4, c_pos[1] + 4))
    
    s.blit(sc_sh, sc_sh_rect)
    s.blit(sc_surf, sc_rect)

# --- 5. Fungsi-fungsi Game ---
def reset_chopping_game():
    global current_veggie_cut_count, score, feedback_data, bowl_slices, flying_slices, current_veggie_type, current_veggie_img, current_veggie_slice_img, current_veggie_rect
    current_veggie_cut_count = 0; score = 0; feedback_data["text"] = ""; bowl_slices = []; flying_slices = []
    current_veggie_type = "timun"; current_veggie_img = VEGGIE1_FULL_IMG; current_veggie_slice_img = VEGGIE1_SLICE_IMG
    current_veggie_rect = current_veggie_img.get_rect(center=cutting_board_rect.center)

def start_game(): global current_screen; current_screen = "game"; reset_chopping_game()

def switch_veggie():
    global current_veggie_type, current_veggie_img, current_veggie_slice_img, current_veggie_rect, current_veggie_cut_count, bowl_slices, flying_slices
    current_veggie_cut_count = 0; bowl_slices = []; flying_slices = [] 
    if current_veggie_type == "timun": current_veggie_type = "terong"; current_veggie_img = VEGGIE2_FULL_IMG; current_veggie_slice_img = VEGGIE2_SLICE_IMG
    else: current_veggie_type = "timun"; current_veggie_img = VEGGIE1_FULL_IMG; current_veggie_slice_img = VEGGIE1_SLICE_IMG
    current_veggie_rect = current_veggie_img.get_rect(center=cutting_board_rect.center)

def start_flying_slice(start_pos):
    if len(bowl_slices) < len(bowl_positions): 
        target_index = len(bowl_slices); relative_target_pos = bowl_positions[target_index]
        target_pos = (bowl_rect.left + relative_target_pos[0], bowl_rect.top + relative_target_pos[1])
        flying_slices.append({"img": current_veggie_slice_img, "start_pos": list(start_pos), "current_pos": list(start_pos), "target_pos": target_pos, "rotation": random.randint(-180, 180), "start_time": pygame.time.get_ticks(), "duration": 400})

def add_slice_to_bowl(slice_data):
    if len(bowl_slices) < len(bowl_positions):
         bowl_slices.append({"img": slice_data["img"], "pos": slice_data["target_pos"], "rotation": random.randint(-5, 5), "alpha": 255, "fade_in_start": pygame.time.get_ticks()}) 

# --- 6. Game Loop Utama ---
running = True
while running:
    
    current_time = pygame.time.get_ticks()
    mouse_pos = pygame.mouse.get_pos()
    
    pulse = (math.sin(current_time * 0.005) + 1) / 2 
    slow_pulse = (math.sin(current_time * 0.002) + 1) / 2 

    # --- 7. Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        
        if current_screen == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button_rect.collidepoint(event.pos): start_game()
                elif settings_button_rect.collidepoint(event.pos): current_screen = "settings"
        
        elif current_screen == "settings":
             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 if back_button_rect.collidepoint(event.pos): current_screen = "menu"

        elif current_screen == "game":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if cutting_board_rect.collidepoint(event.pos): is_dragging_cut = True; cut_start_pos = event.pos; cut_end_pos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if is_dragging_cut: cut_end_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if is_dragging_cut:
                    is_dragging_cut = False; dx = cut_end_pos[0] - cut_start_pos[0]; dy = cut_end_pos[1] - cut_start_pos[1]; distance = math.hypot(dx, dy)
                    if distance > MIN_DRAG_DISTANCE:
                        did_cut = current_veggie_rect.clipline(cut_start_pos, cut_end_pos); is_horizontal_cut = abs(dx) > abs(dy) * 1.5
                        if did_cut and is_horizontal_cut:
                            score += 1; current_veggie_cut_count += 1; feedback_data = {"text": "NICE!", "color": GREEN_LIGHT, "start_time": current_time, "duration": 800, "y_offset": 0, "alpha": 255}
                            cut_mid_pos = ((cut_start_pos[0] + cut_end_pos[0]) // 2, (cut_start_pos[1] + cut_end_pos[1]) // 2); start_flying_slice(cut_mid_pos)
                            if current_veggie_cut_count >= MAX_CUTS_PER_VEGGIE: switch_veggie()
                        else: feedback_data = {"text": "OOPS!", "color": RED_CRITICAL, "start_time": current_time, "duration": 800, "y_offset": 0, "alpha": 255}
                    else: feedback_data = {"text": "OOPS!", "color": RED_CRITICAL, "start_time": current_time, "duration": 800, "y_offset": 0, "alpha": 255}

    # --- 8. Logika Update ---
    if current_screen == "menu":
         for sparkle in menu_sparkles:
            if current_time - sparkle["born"] > sparkle["life"]:
                sparkle["pos"] = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]; sparkle["born"] = current_time; sparkle["life"] = random.randint(500, 1500)

    elif current_screen == "game":
        if feedback_data["text"]:
            elapsed_feedback = current_time - feedback_data["start_time"]
            if elapsed_feedback < feedback_data["duration"]: t_fade = elapsed_feedback / feedback_data["duration"]; feedback_data["y_offset"] = -60 * t_fade; feedback_data["alpha"] = int(255 * (1 - t_fade))
            else: feedback_data["text"] = ""

        for flying_slice in reversed(flying_slices):
            elapsed = current_time - flying_slice["start_time"]
            if elapsed >= flying_slice["duration"]: add_slice_to_bowl(flying_slice); flying_slices.remove(flying_slice)
            else:
                t = elapsed / flying_slice["duration"]; flying_slice["current_pos"][0] = flying_slice["start_pos"][0] + (flying_slice["target_pos"][0] - flying_slice["start_pos"][0]) * t; flying_slice["current_pos"][1] = flying_slice["start_pos"][1] + (flying_slice["target_pos"][1] - flying_slice["start_pos"][1]) * t; flying_slice["rotation"] += 15
        
        sunbeam_surf.fill((0, 0, 0, 0)) 
        beam_pulse = (math.sin(current_time * 0.001) + 1) / 2 
        for i in range(NUM_BEAMS):
            angle = beam_angles[i] + math.sin(current_time * 0.0005 + i) * 0.05 
            end_x = SUNBEAM_ORIGIN[0] + math.cos(angle) * 1000 
            end_y = SUNBEAM_ORIGIN[1] + math.sin(angle) * 1000
            base_x1 = SUNBEAM_ORIGIN[0] + math.cos(angle - 0.02) * 20
            base_y1 = SUNBEAM_ORIGIN[1] + math.sin(angle - 0.02) * 20
            base_x2 = SUNBEAM_ORIGIN[0] + math.cos(angle + 0.02) * 20
            base_y2 = SUNBEAM_ORIGIN[1] + math.sin(angle + 0.02) * 20
            beam_points = [ (base_x1, base_y1), (base_x2, base_y2), (end_x, end_y) ] 
            current_alpha = int(beam_alphas[i] * (0.5 + beam_pulse * 0.5)) 
            beam_color = SUNBEAM_COLOR[:3] + (current_alpha,) 
            pygame.draw.polygon(sunbeam_surf, beam_color, beam_points)


    # --- 9. Render (Menggambar ke Layar) ---
    if current_screen == "menu":
        SCREEN.blit(BG_MENU, (0, 0))

        for sparkle in menu_sparkles:
            life_ratio = (current_time - sparkle["born"]) / sparkle["life"]; alpha = int(math.sin(life_ratio * math.pi) * 100); color_with_alpha = sparkle["color"][:3] + (alpha,); pygame.draw.circle(SCREEN, color_with_alpha, sparkle["pos"], sparkle["radius"])

        title_scale = 1.0 + (slow_pulse * 0.05); title_surf = FONT_TITLE.render("Cooking Time!", True, PURPLE_SOFT); title_shadow_surf = FONT_TITLE.render("Cooking Time!", True, TEXT_SHADOW)
        draw_pulsing_text(SCREEN, title_surf, title_shadow_surf, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), title_scale)

        button_scale = 1.0 + (pulse * 0.03) 
        scaled_button_rect = pygame.Rect(0,0, int(play_button_rect.width * button_scale), int(play_button_rect.height * button_scale))
        scaled_button_rect.center = play_button_rect.center 
        button_surf = pygame.Surface(scaled_button_rect.size, pygame.SRCALPHA); pygame.draw.rect(button_surf, MENU_BUTTON_BG, button_surf.get_rect(), border_radius=15); SCREEN.blit(button_surf, scaled_button_rect.topleft)
        pygame.draw.rect(SCREEN, MENU_BUTTON_BORDER, scaled_button_rect, width=3, border_radius=15)
        play_text = FONT_BUTTON.render("Mulai Memasak", True, WHITE); play_text_rect = play_text.get_rect(center=scaled_button_rect.center); SCREEN.blit(play_text, play_text_rect)
        
        settings_text = FONT_BUTTON.render("Pengaturan", True, WHITE)
        settings_button_rect = pygame.Rect(0, 0, settings_text.get_width() + 30, settings_text.get_height() + 15)
        settings_button_rect.bottomright = (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15) 
        settings_btn_col = MENU_BUTTON_BG 
        if settings_button_rect.collidepoint(mouse_pos): settings_btn_col = (MENU_BUTTON_BG[0]+20, MENU_BUTTON_BG[1]+20, MENU_BUTTON_BG[2]+20, MENU_BUTTON_BG[3])
        settings_surf = pygame.Surface(settings_button_rect.size, pygame.SRCALPHA); pygame.draw.rect(settings_surf, settings_btn_col, settings_surf.get_rect(), border_radius=10); SCREEN.blit(settings_surf, settings_button_rect.topleft)
        pygame.draw.rect(SCREEN, MENU_BUTTON_BORDER, settings_button_rect, width=2, border_radius=10)
        SCREEN.blit(settings_text, settings_text.get_rect(center=settings_button_rect.center))

    elif current_screen == "settings":
        SCREEN.fill(SETTINGS_BG_COLOR)
        st_text = FONT_SETTINGS_TITLE.render("PENGATURAN", True, WHITE); st_rect = st_text.get_rect(center=(SCREEN_WIDTH // 2, 100)); SCREEN.blit(st_text, st_rect)
        u_text = FONT_BUTTON.render("- Umum (Belum Ada Isi) -", True, WHITE); u_rect = u_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)); SCREEN.blit(u_text, u_rect)

        back_text = FONT_BUTTON.render("Kembali", True, WHITE); 
        back_button_rect = pygame.Rect(0, 0, back_text.get_width() + 30, back_text.get_height() + 15)
        back_button_rect.bottomright = (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15)
        back_btn_col = MENU_BUTTON_BG
        if back_button_rect.collidepoint(mouse_pos): back_btn_col = (MENU_BUTTON_BG[0]+20, MENU_BUTTON_BG[1]+20, MENU_BUTTON_BG[2]+20, MENU_BUTTON_BG[3])
        back_surf = pygame.Surface(back_button_rect.size, pygame.SRCALPHA); pygame.draw.rect(back_surf, back_btn_col, back_surf.get_rect(), border_radius=10); SCREEN.blit(back_surf, back_button_rect.topleft)
        pygame.draw.rect(SCREEN, MENU_BUTTON_BORDER, back_button_rect, width=2, border_radius=10)
        SCREEN.blit(back_text, back_text.get_rect(center=back_button_rect.center))

    elif current_screen == "game":
        SCREEN.blit(BG_GAME, (0, 0))
        SCREEN.blit(sunbeam_surf, (0,0)) 
        
        SCREEN.blit(CUTTING_BOARD_IMG, cutting_board_rect)
        SCREEN.blit(BOWL_IMG, bowl_rect)

        for s in bowl_slices:
            slice_surface = pygame.Surface(s["img"].get_size(), pygame.SRCALPHA); slice_surface.blit(s["img"], (0,0)); slice_surface.set_alpha(s["alpha"])
            slice_img_rotated = pygame.transform.rotate(slice_surface, s["rotation"]); SCREEN.blit(slice_img_rotated, s["pos"]) 
        
        for fs in flying_slices:
            fs_surf = pygame.transform.rotate(fs["img"], fs["rotation"]); fs_rect = fs_surf.get_rect(center=fs["current_pos"]); SCREEN.blit(fs_surf, fs_rect)

        SCREEN.blit(current_veggie_img, current_veggie_rect)

        if is_dragging_cut:
            dx = cut_end_pos[0] - cut_start_pos[0]; dy = cut_end_pos[1] - cut_start_pos[1]; angle = math.degrees(math.atan2(-dy, dx))
            rotated_knife = pygame.transform.rotate(KNIFE_IMG, angle); knife_rect = rotated_knife.get_rect(center=cut_end_pos); SCREEN.blit(rotated_knife, knife_rect)

        score_text = FONT_SMALL.render(f"SCORE: {score}", True, BLACK); cut_count_text = FONT_SMALL.render(f"DIPOTONG: {current_veggie_cut_count}/{MAX_CUTS_PER_VEGGIE}", True, BLACK)
        ui_panel_height = score_text.get_height() + cut_count_text.get_height() + 30; ui_panel_width = max(score_text.get_width(), cut_count_text.get_width()) + 30; ui_panel_rect = pygame.Rect(5, 5, ui_panel_width, ui_panel_height)
        ui_panel_surface = pygame.Surface(ui_panel_rect.size, pygame.SRCALPHA); ui_panel_surface.fill(UI_PANEL_COLOR); pygame.draw.rect(ui_panel_surface, (255,100,150, 180), ui_panel_surface.get_rect(), 3, border_radius=5)
        SCREEN.blit(ui_panel_surface, ui_panel_rect.topleft); SCREEN.blit(score_text, (ui_panel_rect.x + 15, ui_panel_rect.y + 10)); SCREEN.blit(cut_count_text, (ui_panel_rect.x + 15, ui_panel_rect.y + 10 + score_text.get_height() + 5))

        if feedback_data["text"]:
            feedback_surf = FONT_FEEDBACK.render(feedback_data["text"], True, feedback_data["color"]); feedback_shadow = FONT_FEEDBACK.render(feedback_data["text"], True, TEXT_SHADOW)
            feedback_surf.set_alpha(feedback_data["alpha"]); feedback_shadow.set_alpha(feedback_data["alpha"])
            feedback_shadow_rect = feedback_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 4, SCREEN_HEIGHT // 2 - 120 + 4 + feedback_data["y_offset"])); SCREEN.blit(feedback_shadow, feedback_shadow_rect)
            feedback_rect = feedback_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120 + feedback_data["y_offset"])); SCREEN.blit(feedback_surf, feedback_rect)

    # --- 10. Update Tampilan ---
    pygame.display.flip()
    clock.tick(60)

# --- 11. Keluar ---
pygame.quit()
print("Game Cooking Time ditutup.")

# AKHIR KODE
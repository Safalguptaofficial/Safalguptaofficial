#!/usr/bin/env python3
"""
SAFAL_OS Biosphere Physics Engine
Simulates fish behavior, hunger mechanics, and ecosystem balance
"""

import json
import random
import math
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import svgwrite

class Fish:
    def __init__(self, username: str, x: float = None, y: float = None):
        self.id = username
        self.x = x or random.uniform(50, 750)
        self.y = y or random.uniform(50, 350)
        # Velocity vector
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0.5, 2.0)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        # Biological stats
        self.hunger = 100  # 0 = dead
        self.size = 10 + min(len(username) * 0.5, 15)  # Size based on username length (just for variety)
        self.color = self._generate_color(username)
        self.last_fed = datetime.now().isoformat()
        
    def _generate_color(self, username: str) -> str:
        """Generate deterministic color from username"""
        hash_val = sum(ord(c) * (i + 1) for i, c in enumerate(username))
        hue = hash_val % 360
        return f"hsl({hue}, 70%, 50%)"
    
    def update(self, width: float = 800, height: float = 400, 
               food_list: List[Dict] = None, algae_level: float = 0) -> bool:
        """
        Update fish physics. Returns False if fish dies.
        """
        # Boids algorithm (simplified): seek food if hungry, wander otherwise
        if food_list and self.hunger < 80:
            # Find nearest food
            nearest = min(food_list, key=lambda f: math.hypot(f['x'] - self.x, f['y'] - self.y))
            dx = nearest['x'] - self.x
            dy = nearest['y'] - self.y
            dist = math.hypot(dx, dy)
            if dist > 0:
                self.vx += (dx / dist) * 0.3
                self.vy += (dy / dist) * 0.3
        
        # Random wandering (Perlin noise substitute)
        self.vx += random.uniform(-0.2, 0.2)
        self.vy += random.uniform(-0.2, 0.2)
        
        # Speed limit
        speed = math.hypot(self.vx, self.vy)
        if speed > 3.0:
            self.vx = (self.vx / speed) * 3.0
            self.vy = (self.vy / speed) * 3.0
        
        # Update position
        self.x += self.vx
        self.y += self.vy
        
        # Boundary collision (bounce)
        if self.x < 20 or self.x > width - 20:
            self.vx *= -1
            self.x = max(20, min(width - 20, self.x))
        if self.y < 20 or self.y > height - 20:
            self.vy *= -1
            self.y = max(20, min(height - 20, self.y))
        
        # Metabolism
        self.hunger -= 0.5  # Decay per tick (5 min)
        if algae_level > 50:
            self.hunger -= 0.2  # Algae helps (oxygen correlation)
            
        return self.hunger > 0

class BiosphereEngine:
    def __init__(self, state_file: str):
        self.width = 800
        self.height = 400
        self.load_state(state_file)
    
    def load_state(self, filepath: str):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            self.fish = [Fish(f['id'], f['x'], f['y']) for f in data.get('fish', [])]
            # Restore stats
            for i, f_data in enumerate(data.get('fish', [])):
                if i < len(self.fish):
                    self.fish[i].hunger = f_data.get('hunger', 100)
                    self.fish[i].vx = f_data.get('vx', 0)
                    self.fish[i].vy = f_data.get('vy', 0)
            
            self.food = data.get('food', [])
            self.algae = data.get('algae', 0)
            self.generation = data.get('generation', 0)
        except FileNotFoundError:
            self.fish = []
            self.food = []
            self.algae = 0
            self.generation = 0
    
    def add_fish(self, username: str):
        """Spawn new visitor as fish"""
        # Prevent duplicates
        if not any(f.id == username for f in self.fish):
            self.fish.append(Fish(username))
    
    def add_food(self, issue_title: str):
        """Convert issue into food pellet"""
        x = random.uniform(50, self.width - 50)
        y = 0  # Drops from top
        nutrition = 20 + min(len(issue_title), 50)  # Longer issues = more food (engagement reward)
        self.food.append({'x': x, 'y': y, 'nutrition': nutrition, 'id': random.randint(1000, 9999)})
    
    def update(self):
        """Main game tick"""
        self.generation += 1
        
        # Update fish
        alive_fish = []
        for fish in self.fish:
            if fish.update(self.width, self.height, self.food, self.algae):
                alive_fish.append(fish)
                
                # Check food collision
                for food in self.food[:]:
                    if math.hypot(fish.x - food['x'], fish.y - food['y']) < 15:
                        fish.hunger = min(100, fish.hunger + food['nutrition'])
                        fish.last_fed = datetime.now().isoformat()
                        self.food.remove(food)
                        break
        
        self.fish = alive_fish
        
        # Update food (gravity)
        for food in self.food:
            food['y'] += 2  # Fall speed
            if food['y'] > self.height:
                food['y'] = self.height
                food['nutrition'] -= 1  # Decay on ground
        
        self.food = [f for f in self.food if f['nutrition'] > 0]
        
        # Algae growth based on commit velocity (from metrics.json)
        # In real implementation, read from metrics.json
        self.algae = min(100, self.algae + 0.1)  # Slow growth
    
    def render_svg(self, output_path: str):
        """Generate animated SVG using SMIL (works in GitHub markdown)"""
        dwg = svgwrite.Drawing(output_path, size=(self.width, self.height))
        
        # Background gradient (water quality based on algae)
        water_color = "#0d1117" if self.algae < 50 else "#1a2f1a"
        dwg.add(dwg.rect(insert=(0, 0), size=(self.width, self.height), fill=water_color))
        
        # Seaweed (swaying using SMIL animate)
        for i in range(5):
            x = 100 + i * 150
            seaweed = dwg.path(d=f"M {x} 400 Q {x} 350 {x-10} 300", 
                             stroke="#238636", stroke_width=3, fill="none")
            # Animate swaying
            animate = dwg.animate(attributeName="d", 
                                values=f"M {x} 400 Q {x} 350 {x-10} 300;M {x} 400 Q {x+10} 350 {x+10} 300;M {x} 400 Q {x} 350 {x-10} 300",
                                dur=f"{3 + i*0.5}s", repeatCount="indefinite")
            seaweed.add(animate)
            dwg.add(seaweed)
        
        # Food pellets
        for food in self.food:
            circle = dwg.circle(center=(food['x'], food['y']), r=3, fill="#ffa500")
            dwg.add(circle)
        
        # Fish (with SMIL animation for movement)
        for fish in self.fish:
            g = dwg.g()
            
            # Fish body
            body = dwg.ellipse(center=(0, 0), r=(fish.size, fish.size/2), fill=fish.color)
            g.add(body)
            
            # Fish tail (animated)
            tail = dwg.path(d="M -10 0 L -15 -5 L -15 5 Z", fill=fish.color)
            tail_animate = dwg.animateTransform(attributeName="transform", type="rotate",
                                               values="-10 0 0;10 0 0;-10 0 0", dur="0.5s", repeatCount="indefinite")
            tail.add(tail_animate)
            g.add(tail)
            
            # Username label
            text = dwg.text(fish.id[:10], insert=(0, -fish.size-5), 
                          font_size="10px", fill="#c9d1d9", text_anchor="middle",
                          font_family="monospace")
            g.add(text)
            
            # Hunger indicator (opacity based on health)
            health_bar = dwg.rect(insert=(-10, -fish.size-12), size=(20 * (fish.hunger/100), 3), 
                                fill="#ff0000" if fish.hunger < 30 else "#00ff00")
            g.add(health_bar)
            
            # Position using animateMotion for smooth movement
            # Calculate next position for animation direction
            next_x = fish.x + fish.vx * 50  # Look ahead
            next_y = fish.y + fish.vy * 50
            
            # SMIL motion path
            path_data = f"M {fish.x} {fish.y} L {next_x} {next_y}"
            animate_motion = dwg.animateMotion(path=path_data, dur="5s", fill="freeze")
            g.add(animate_motion)
            
            dwg.add(g)
        
        # Overlay: Stats
        stats_text = f"Population: {len(self.fish)} | Generation: {self.generation} | Algae: {self.algae:.1f}%"
        dwg.add(dwg.text(stats_text, insert=(10, 20), fill="#8b949e", 
                        font_size="12px", font_family="monospace"))
        
        # Clock
        time_str = datetime.now().strftime("%H:%M UTC")
        dwg.add(dwg.text(time_str, insert=(self.width-60, 20), fill="#8b949e", 
                        font_size="12px", font_family="monospace"))
        
        # In renderer.py, add invisible text in SVG (Layer 7):
        if self.generation % 100 == 0:  # Every ~8 hours
            dwg.add(dwg.text("Layer 7: The fish know your secrets. Check the reflog.", 
                            insert=(400, 200), opacity=0, 
                            id="hidden-layer-7"))

        dwg.save()
    
    def save_state(self, filepath: str):
        state = {
            'fish': [{'id': f.id, 'x': f.x, 'y': f.y, 'vx': f.vx, 'vy': f.vy, 
                     'hunger': f.hunger, 'size': f.size} for f in self.fish],
            'food': self.food,
            'algae': self.algae,
            'generation': self.generation,
            'timestamp': datetime.now().isoformat(),
            'population': len(self.fish)
        }
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state', required=True)
    parser.add_argument('--new-stars', default=None)
    parser.add_argument('--new-issues', default=None)
    parser.add_argument('--output-state', required=True)
    parser.add_argument('--output-svg', required=True)
    args = parser.parse_args()
    
    engine = BiosphereEngine(args.state)
    
    # Process new stars
    if args.new_stars:
        try:
            with open(args.new_stars) as f:
                stars = json.load(f)
                for star in stars:
                    engine.add_fish(star['username'])
        except FileNotFoundError:
            pass
    
    # Process issues as food
    if args.new_issues:
        try:
            with open(args.new_issues) as f:
                issues = json.load(f)
                for issue in issues:
                    engine.add_food(issue['title'])
        except FileNotFoundError:
            pass
    
    engine.update()
    engine.render_svg(args.output_svg)
    engine.save_state(args.output_state)

if __name__ == "__main__":
    main()

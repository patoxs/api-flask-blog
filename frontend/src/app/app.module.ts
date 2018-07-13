import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { MenuComponent } from './menu/menu.component';
import { PreloaderComponent } from './preloader/preloader.component';
import { FooterComponent } from './footer/footer.component';
import { FeaturePostComponent } from './feature-post/feature-post.component';
import { MenuContentComponent } from './menu/menu-content/menu-content.component';
import { SocialComponent } from './menu/social/social.component';
import { NewComponent } from './feature-post/new/new.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { HomeComponent } from './home/home.component';
import { AppRoutingModule } from './app-routing.module';
import { SlidingMenuComponent } from './sliding-menu/sliding-menu.component';
import { NewDetailComponent } from './new-detail/new-detail.component';
import { ScrollspyComponent } from './scrollspy/scrollspy.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    PreloaderComponent,
    FooterComponent,
    FeaturePostComponent,
    MenuContentComponent,
    SocialComponent,
    NewComponent,
    NotFoundComponent,
    HomeComponent,
    SlidingMenuComponent,
    NewDetailComponent,
    ScrollspyComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

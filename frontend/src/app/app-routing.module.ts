import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

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
import { NewDetailComponent } from './new-detail/new-detail.component';

const appRoutes: Routes = [
  { path: '', component: FeaturePostComponent },
  { path: 'news', component: NewDetailComponent },
  { path: '**', component: NotFoundComponent }
]

@NgModule ({
    imports: [
      RouterModule.forRoot(appRoutes)
    ],
    exports: [ RouterModule ]
})

export class AppRoutingModule {

}
